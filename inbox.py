# Copyright (C) 2012- Canonical Ltd
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import random
import hashlib
import email
from email.message import EmailMessage
from email.header import decode_header
import mailbox
import email.utils
from itertools import count
from io import StringIO, BytesIO

from zope.interface import implementer

from twisted.mail import imap4
from twisted.python import log


SEEN = r"\Seen"
UNSEEN = r"\Unseen"
DELETED = r"\Deleted"
FLAGGED = r"\Flagged"
ANSWERED = r"\Answered"
RECENT = r"\Recent"


@implementer(imap4.IMailbox)
class MemoryIMAPMailbox(object):

    mbox = None

    def addMessage(self, msg_fp, flags=None, date=None):
        if flags is None:
            flags = []
        if date is None:
            date = email.utils.formatdate()
        msg = Message(msg_fp, flags, date)
        if self.mbox is not None:
            self.mbox.add(msg.msg)
        self.msgs.append(msg)
        self.flush()

    def setFile(self, path):
        log.msg("creating mbox file %s" % path)
        self.mbox = mailbox.mbox(path)

    def flush(self):
        if self.mbox is not None:
            log.msg("flushing mailbox")
            self.mbox.flush()

    def _load_message_from_api(self, msg):
        message = self.api.mail_id_get(msg.id)
        message.subject = message.subject.encode("ascii", "ignore").decode()
        self.msgs.append(Message(message, [], message.date_time))

    def __init__(self, initial_messages, api_client, category):
        self.api = api_client
        self.msgs = []
        self.listeners = []
        self.uidvalidity = (
            int(hashlib.sha256(category             .encode("utf-8")).hexdigest(), 16) % 10**8
        )
        self.category = category

        print(f"Loading {len(initial_messages)} messages for {category}")
        for msg in initial_messages:
            self._load_message_from_api(msg)
        print("Loaded %s messages" % len(self.msgs))

    def _get_msgs(self, msg_set, uid):
        if not self.msgs:
            return {}
        if uid:
            msg_set.last = max(x.uid for x in self.msgs)
            uids = set(msg_set)
            return dict((msg.uid, msg) for msg in self.msgs if msg.uid in uids)
        else:
            msg_set.last = max(x.uid for x in self.msgs)
            return dict((msg.uid, msg) for msg in self.msgs if msg.uid in msg_set)

    def getHierarchicalDelimiter(self):
        return "."

    def getFlags(self):
        "return list of flags supported by this mailbox"
        return [SEEN, UNSEEN, DELETED, FLAGGED, ANSWERED, RECENT]

    def getMessageCount(self):
        return len(self.msgs)

    def getRecentCount(self):
        return len(self.msgs)
        # return len([m for m in self.msgs if RECENT in m.getFlags()])

    def getUnseenCount(self):
        return len([m for m in self.msgs if UNSEEN in m.getFlags()])

    def isWriteable(self):
        return True

    def getUIDValidity(self):
        return self.uidvalidity

    def getUID(self, messageNum):
        return messageNum
        # return self.msgs[messageNum - 1].uid

    def getUIDNext(self):
        return max(x.uid for x in self.msgs) + 1

    def fetch(self, msg_set, uid):
        messages = self._get_msgs(msg_set, uid)
        return messages.items()

    def addListener(self, listener):
        self.listeners.append(listener)
        return True

    def removeListener(self, listener):
        self.listeners.remove(listener)
        return True

    def requestStatus(self, path):
        return imap4.statusRequestHelper(self, path)

    def store(self, msg_set, flags, mode, uid):
        messages = self._get_msgs(msg_set, uid)
        setFlags = {}
        for seq, msg in messages.items():
            if mode == 0:  # replace flags
                msg.flags = set(flags)
            else:
                for flag in flags:
                    # mode 1 is append, mode -1 is delete
                    if mode == 1 and flag not in msg.flags:
                        msg.flags.add(flag)
                    elif mode == -1 and flag in msg.flags:
                        msg.flags.remove(flag)
            setFlags[seq] = msg.flags
        return setFlags

    def expunge(self):
        "remove all messages marked for deletion"
        removed = []
        for i, msg in enumerate(self.msgs[:]):
            if DELETED in msg.flags:
                # use less efficient remove() because the indexes are changing
                self.msgs.remove(msg)
                removed.append(msg.uid)
        self.flush()
        return removed

    def destroy(self):
        "complete remove the mailbox and all its contents"
        raise imap4.MailboxException("Permission denied.")


@implementer(imap4.IMessagePart)
class MessagePart(object):

    def __init__(self, msg):
        self.msg = msg

    def getHeaders(self, negate, *names):
        headers = {}
        if negate:
            for header in self.msg.keys():
                if header.upper() not in names:
                    headers[header.lower()] = self.msg.get(header, "")
        else:
            for name in names:
                name = name.decode()
                headers[name.lower()] = self.msg.get(name, "")
        return headers

    def getBodyFile(self):
        if self.msg.is_multipart():
            raise TypeError("Requested body file of a multipart message")
        return BytesIO(self.msg.get_payload().encode())

    def getSize(self):
        return len(self.msg.as_string())

    def isMultipart(self):
        return self.msg.is_multipart()

    def getSubPart(self, part):
        if self.msg.is_multipart():
            return MessagePart(self.msg.get_payload()[part])
        raise TypeError("Not a multipart message")

    def parse_charset(self, default="utf8"):
        charset = self.msg.get_charset()
        if charset is not None:
            return charset

        if self.msg.get("Content-type"):
            for chunk in self.msg["Content-type"].split(";"):
                if "charset" in chunk:
                    return chunk.split("=")[1]
        return default

    def unicode(self, header):
        """Converts a header to unicode"""
        value = self.msg[header]
        orig, enc = decode_header(value)[0]
        if enc is None:
            enc = self.parse_charset()
        return orig.decode(enc)


@implementer(imap4.IMessage)
class Message(MessagePart):

    def __init__(self, original, flags, date):

        email_message = EmailMessage()
        email_message.set_content(original.body)
        email_message["From"] = original._from
        email_message["To"] = original.to
        email_message["Subject"] = original.subject

        super(Message, self).__init__(email_message)
        self.uid = original.id
        self.flags = set(flags)
        self.date = original.date_time

    def getUID(self):
        return self.uid

    def getFlags(self):
        return self.flags

    def getInternalDate(self):
        return self.date

    def __repr__(self):
        h = self.getHeaders(False, "From", "To")
        return "<From: %s, To: %s, Uid: %s>" % (h["from"], h["to"], self.uid)

    def payloads(self):
        for part in self.msg.walk():
            if part.get_content_maintype() == "multipart":
                continue
            payload = part.get_payload(decode=True)
            enc = self.parse_charset()
            yield payload.decode(enc)
