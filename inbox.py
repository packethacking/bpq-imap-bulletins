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

import httpdate
import structlog

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

    def __init__(self, initial_messages, api_client, category, callsign):
        self.api = api_client
        self.msgs = []
        self.listeners = []
        self.uidvalidity = (
            int(hashlib.sha256(category.encode("utf-8")).hexdigest(), 16) % 10**8
        )
        self.category = category
        self.account_identifier = "".join(
            random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=4)
        )
        self.logger = structlog.get_logger().bind(
            category=category,
            callsign=callsign,
            account_identifier=self.account_identifier,
        )

        self.logger.info(f"Loading {len(initial_messages)} messages")
        self.update_mailbox(initial_messages)
        self.logger.info(f"Loaded {len(self.msgs)} messages")

    def update_mailbox(self, msgs):
        ids_to_fetch = [str(x.id) for x in msgs]
        if not ids_to_fetch:
            self.logger.info("No messages to fetch")
            return
        self.logger.info(f"Fetching messages: {ids_to_fetch}")
        messages = self.api.mail_ids_get(",".join(ids_to_fetch))
        fetched = [x.id for x in messages]
        self.logger.info(f"Fetched {len(fetched)} messages")
        for msg in messages:
            msg.subject = (
                msg.subject.encode("ascii", "ignore").decode() if msg.subject else ""
            )
            self.msgs.append(Message(msg, [], msg.date_time))

    def _get_msgs(self, msg_set, uid):
        if not self.msgs:
            return {}

        if uid:
            msg_set.last = self.getUIDNext()
            self.logger.info(f"Fetching by UID: {msg_set}")
            result = {
                msg.uid: msg for msg in self.msgs if msg.uid and msg.uid in msg_set
            }
            self.logger.info(f"Found {len(result)} messages")
            return result
        return {i: self.msgs[i - 1] for i in msg_set}

    def getHierarchicalDelimiter(self):
        return "."

    def getFlags(self):
        "return list of flags supported by this mailbox"
        return [SEEN, UNSEEN, DELETED, FLAGGED, ANSWERED, RECENT]

    def getMessageCount(self):
        self.logger.info(f"Getting message count: {len(self.msgs)}")
        return len(self.msgs)

    def getRecentCount(self):
        self.logger.info(f"Getting recent count: {len(self.msgs)}")
        return len(self.msgs)
        # return len([m for m in self.msgs if RECENT in m.getFlags()])

    def getUnseenCount(self):
        self.logger.info(f"Getting unseen count: {len(self.msgs)}")
        return len([m for m in self.msgs if UNSEEN in m.getFlags()])

    def isWriteable(self):
        return True

    def getUIDValidity(self):
        return self.uidvalidity

    def getUID(self, messageNum):
        try:
            uid = self.msgs[messageNum].uid
            self.logger.info(f"Getting UID for message {messageNum}: {uid}")
            return self.msgs[messageNum].uid
        except IndexError:
            self.logger.info(f"Message {messageNum} not found")
            return None

    def getUIDNext(self):
        self.logger.info(f"Getting next UID:")
        return max([m.uid for m in self.msgs if m.uid], default=0) + 1

    def fetch(self, msg_set, uid):
        self.logger.info(f"Fetching messages: {msg_set}")
        messages = self._get_msgs(msg_set, uid)
        result = sorted([(k, v) for k, v in messages.items()], key=lambda x: x[0])
        return result

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
                name = name.decode() if isinstance(name, bytes) else name
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
        email_message.set_content(original.body if original.body else "")
        email_message["From"] = original._from.replace(".#", ".hash")
        email_message["To"] = original.to.replace(".#", ".hash")
        email_message["Subject"] = original.subject
        email_message["Date"] = email.utils.formatdate(date.timestamp())
        super(Message, self).__init__(email_message)

        self.uid = original.id
        self.flags = set(flags)
        self.date = httpdate.unixtime_to_httpdate(
            int(original.date_time.timestamp() if original.date_time else 0)
        )

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
