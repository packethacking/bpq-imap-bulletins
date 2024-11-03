# coding: utf-8

"""
    BPQ API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NativeForwardingConfigV1(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'queue_length': 'int',
        'to': 'list[str]',
        'at': 'list[str]',
        'hrp': 'list[str]',
        'hrb': 'list[str]',
        'times': 'list[str]',
        'connect_script': 'list[str]',
        'bbs_ha': 'str',
        'enable_forwarding': 'bool',
        'forwarding_interval': 'TimeSpan',
        'request_reverse': 'bool',
        'reverse_interval': 'TimeSpan',
        'send_new_messages_without_waiting': 'bool',
        'fbb_blocked': 'bool',
        'max_block': 'int',
        'send_personal_mail_only': 'bool',
        'allow_binary': 'bool',
        'use_b1_protocol': 'bool',
        'use_b2_protocol': 'bool',
        'incoming_connect_timeout': 'TimeSpan'
    }

    attribute_map = {
        'queue_length': 'queueLength',
        'to': 'to',
        'at': 'at',
        'hrp': 'hrp',
        'hrb': 'hrb',
        'times': 'times',
        'connect_script': 'connectScript',
        'bbs_ha': 'bbsHa',
        'enable_forwarding': 'enableForwarding',
        'forwarding_interval': 'forwardingInterval',
        'request_reverse': 'requestReverse',
        'reverse_interval': 'reverseInterval',
        'send_new_messages_without_waiting': 'sendNewMessagesWithoutWaiting',
        'fbb_blocked': 'fbbBlocked',
        'max_block': 'maxBlock',
        'send_personal_mail_only': 'sendPersonalMailOnly',
        'allow_binary': 'allowBinary',
        'use_b1_protocol': 'useB1Protocol',
        'use_b2_protocol': 'useB2Protocol',
        'incoming_connect_timeout': 'incomingConnectTimeout'
    }

    def __init__(self, queue_length=None, to=None, at=None, hrp=None, hrb=None, times=None, connect_script=None, bbs_ha=None, enable_forwarding=None, forwarding_interval=None, request_reverse=None, reverse_interval=None, send_new_messages_without_waiting=None, fbb_blocked=None, max_block=None, send_personal_mail_only=None, allow_binary=None, use_b1_protocol=None, use_b2_protocol=None, incoming_connect_timeout=None):  # noqa: E501
        """NativeForwardingConfigV1 - a model defined in Swagger"""  # noqa: E501
        self._queue_length = None
        self._to = None
        self._at = None
        self._hrp = None
        self._hrb = None
        self._times = None
        self._connect_script = None
        self._bbs_ha = None
        self._enable_forwarding = None
        self._forwarding_interval = None
        self._request_reverse = None
        self._reverse_interval = None
        self._send_new_messages_without_waiting = None
        self._fbb_blocked = None
        self._max_block = None
        self._send_personal_mail_only = None
        self._allow_binary = None
        self._use_b1_protocol = None
        self._use_b2_protocol = None
        self._incoming_connect_timeout = None
        self.discriminator = None
        if queue_length is not None:
            self.queue_length = queue_length
        if to is not None:
            self.to = to
        if at is not None:
            self.at = at
        if hrp is not None:
            self.hrp = hrp
        if hrb is not None:
            self.hrb = hrb
        if times is not None:
            self.times = times
        if connect_script is not None:
            self.connect_script = connect_script
        if bbs_ha is not None:
            self.bbs_ha = bbs_ha
        if enable_forwarding is not None:
            self.enable_forwarding = enable_forwarding
        if forwarding_interval is not None:
            self.forwarding_interval = forwarding_interval
        if request_reverse is not None:
            self.request_reverse = request_reverse
        if reverse_interval is not None:
            self.reverse_interval = reverse_interval
        if send_new_messages_without_waiting is not None:
            self.send_new_messages_without_waiting = send_new_messages_without_waiting
        if fbb_blocked is not None:
            self.fbb_blocked = fbb_blocked
        if max_block is not None:
            self.max_block = max_block
        if send_personal_mail_only is not None:
            self.send_personal_mail_only = send_personal_mail_only
        if allow_binary is not None:
            self.allow_binary = allow_binary
        if use_b1_protocol is not None:
            self.use_b1_protocol = use_b1_protocol
        if use_b2_protocol is not None:
            self.use_b2_protocol = use_b2_protocol
        if incoming_connect_timeout is not None:
            self.incoming_connect_timeout = incoming_connect_timeout

    @property
    def queue_length(self):
        """Gets the queue_length of this NativeForwardingConfigV1.  # noqa: E501


        :return: The queue_length of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: int
        """
        return self._queue_length

    @queue_length.setter
    def queue_length(self, queue_length):
        """Sets the queue_length of this NativeForwardingConfigV1.


        :param queue_length: The queue_length of this NativeForwardingConfigV1.  # noqa: E501
        :type: int
        """

        self._queue_length = queue_length

    @property
    def to(self):
        """Gets the to of this NativeForwardingConfigV1.  # noqa: E501


        :return: The to of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this NativeForwardingConfigV1.


        :param to: The to of this NativeForwardingConfigV1.  # noqa: E501
        :type: list[str]
        """

        self._to = to

    @property
    def at(self):
        """Gets the at of this NativeForwardingConfigV1.  # noqa: E501


        :return: The at of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._at

    @at.setter
    def at(self, at):
        """Sets the at of this NativeForwardingConfigV1.


        :param at: The at of this NativeForwardingConfigV1.  # noqa: E501
        :type: list[str]
        """

        self._at = at

    @property
    def hrp(self):
        """Gets the hrp of this NativeForwardingConfigV1.  # noqa: E501


        :return: The hrp of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._hrp

    @hrp.setter
    def hrp(self, hrp):
        """Sets the hrp of this NativeForwardingConfigV1.


        :param hrp: The hrp of this NativeForwardingConfigV1.  # noqa: E501
        :type: list[str]
        """

        self._hrp = hrp

    @property
    def hrb(self):
        """Gets the hrb of this NativeForwardingConfigV1.  # noqa: E501


        :return: The hrb of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._hrb

    @hrb.setter
    def hrb(self, hrb):
        """Sets the hrb of this NativeForwardingConfigV1.


        :param hrb: The hrb of this NativeForwardingConfigV1.  # noqa: E501
        :type: list[str]
        """

        self._hrb = hrb

    @property
    def times(self):
        """Gets the times of this NativeForwardingConfigV1.  # noqa: E501


        :return: The times of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._times

    @times.setter
    def times(self, times):
        """Sets the times of this NativeForwardingConfigV1.


        :param times: The times of this NativeForwardingConfigV1.  # noqa: E501
        :type: list[str]
        """

        self._times = times

    @property
    def connect_script(self):
        """Gets the connect_script of this NativeForwardingConfigV1.  # noqa: E501


        :return: The connect_script of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: list[str]
        """
        return self._connect_script

    @connect_script.setter
    def connect_script(self, connect_script):
        """Sets the connect_script of this NativeForwardingConfigV1.


        :param connect_script: The connect_script of this NativeForwardingConfigV1.  # noqa: E501
        :type: list[str]
        """

        self._connect_script = connect_script

    @property
    def bbs_ha(self):
        """Gets the bbs_ha of this NativeForwardingConfigV1.  # noqa: E501


        :return: The bbs_ha of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: str
        """
        return self._bbs_ha

    @bbs_ha.setter
    def bbs_ha(self, bbs_ha):
        """Sets the bbs_ha of this NativeForwardingConfigV1.


        :param bbs_ha: The bbs_ha of this NativeForwardingConfigV1.  # noqa: E501
        :type: str
        """

        self._bbs_ha = bbs_ha

    @property
    def enable_forwarding(self):
        """Gets the enable_forwarding of this NativeForwardingConfigV1.  # noqa: E501


        :return: The enable_forwarding of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: bool
        """
        return self._enable_forwarding

    @enable_forwarding.setter
    def enable_forwarding(self, enable_forwarding):
        """Sets the enable_forwarding of this NativeForwardingConfigV1.


        :param enable_forwarding: The enable_forwarding of this NativeForwardingConfigV1.  # noqa: E501
        :type: bool
        """

        self._enable_forwarding = enable_forwarding

    @property
    def forwarding_interval(self):
        """Gets the forwarding_interval of this NativeForwardingConfigV1.  # noqa: E501


        :return: The forwarding_interval of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: TimeSpan
        """
        return self._forwarding_interval

    @forwarding_interval.setter
    def forwarding_interval(self, forwarding_interval):
        """Sets the forwarding_interval of this NativeForwardingConfigV1.


        :param forwarding_interval: The forwarding_interval of this NativeForwardingConfigV1.  # noqa: E501
        :type: TimeSpan
        """

        self._forwarding_interval = forwarding_interval

    @property
    def request_reverse(self):
        """Gets the request_reverse of this NativeForwardingConfigV1.  # noqa: E501


        :return: The request_reverse of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: bool
        """
        return self._request_reverse

    @request_reverse.setter
    def request_reverse(self, request_reverse):
        """Sets the request_reverse of this NativeForwardingConfigV1.


        :param request_reverse: The request_reverse of this NativeForwardingConfigV1.  # noqa: E501
        :type: bool
        """

        self._request_reverse = request_reverse

    @property
    def reverse_interval(self):
        """Gets the reverse_interval of this NativeForwardingConfigV1.  # noqa: E501


        :return: The reverse_interval of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: TimeSpan
        """
        return self._reverse_interval

    @reverse_interval.setter
    def reverse_interval(self, reverse_interval):
        """Sets the reverse_interval of this NativeForwardingConfigV1.


        :param reverse_interval: The reverse_interval of this NativeForwardingConfigV1.  # noqa: E501
        :type: TimeSpan
        """

        self._reverse_interval = reverse_interval

    @property
    def send_new_messages_without_waiting(self):
        """Gets the send_new_messages_without_waiting of this NativeForwardingConfigV1.  # noqa: E501


        :return: The send_new_messages_without_waiting of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: bool
        """
        return self._send_new_messages_without_waiting

    @send_new_messages_without_waiting.setter
    def send_new_messages_without_waiting(self, send_new_messages_without_waiting):
        """Sets the send_new_messages_without_waiting of this NativeForwardingConfigV1.


        :param send_new_messages_without_waiting: The send_new_messages_without_waiting of this NativeForwardingConfigV1.  # noqa: E501
        :type: bool
        """

        self._send_new_messages_without_waiting = send_new_messages_without_waiting

    @property
    def fbb_blocked(self):
        """Gets the fbb_blocked of this NativeForwardingConfigV1.  # noqa: E501


        :return: The fbb_blocked of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: bool
        """
        return self._fbb_blocked

    @fbb_blocked.setter
    def fbb_blocked(self, fbb_blocked):
        """Sets the fbb_blocked of this NativeForwardingConfigV1.


        :param fbb_blocked: The fbb_blocked of this NativeForwardingConfigV1.  # noqa: E501
        :type: bool
        """

        self._fbb_blocked = fbb_blocked

    @property
    def max_block(self):
        """Gets the max_block of this NativeForwardingConfigV1.  # noqa: E501


        :return: The max_block of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: int
        """
        return self._max_block

    @max_block.setter
    def max_block(self, max_block):
        """Sets the max_block of this NativeForwardingConfigV1.


        :param max_block: The max_block of this NativeForwardingConfigV1.  # noqa: E501
        :type: int
        """

        self._max_block = max_block

    @property
    def send_personal_mail_only(self):
        """Gets the send_personal_mail_only of this NativeForwardingConfigV1.  # noqa: E501


        :return: The send_personal_mail_only of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: bool
        """
        return self._send_personal_mail_only

    @send_personal_mail_only.setter
    def send_personal_mail_only(self, send_personal_mail_only):
        """Sets the send_personal_mail_only of this NativeForwardingConfigV1.


        :param send_personal_mail_only: The send_personal_mail_only of this NativeForwardingConfigV1.  # noqa: E501
        :type: bool
        """

        self._send_personal_mail_only = send_personal_mail_only

    @property
    def allow_binary(self):
        """Gets the allow_binary of this NativeForwardingConfigV1.  # noqa: E501


        :return: The allow_binary of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: bool
        """
        return self._allow_binary

    @allow_binary.setter
    def allow_binary(self, allow_binary):
        """Sets the allow_binary of this NativeForwardingConfigV1.


        :param allow_binary: The allow_binary of this NativeForwardingConfigV1.  # noqa: E501
        :type: bool
        """

        self._allow_binary = allow_binary

    @property
    def use_b1_protocol(self):
        """Gets the use_b1_protocol of this NativeForwardingConfigV1.  # noqa: E501


        :return: The use_b1_protocol of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: bool
        """
        return self._use_b1_protocol

    @use_b1_protocol.setter
    def use_b1_protocol(self, use_b1_protocol):
        """Sets the use_b1_protocol of this NativeForwardingConfigV1.


        :param use_b1_protocol: The use_b1_protocol of this NativeForwardingConfigV1.  # noqa: E501
        :type: bool
        """

        self._use_b1_protocol = use_b1_protocol

    @property
    def use_b2_protocol(self):
        """Gets the use_b2_protocol of this NativeForwardingConfigV1.  # noqa: E501


        :return: The use_b2_protocol of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: bool
        """
        return self._use_b2_protocol

    @use_b2_protocol.setter
    def use_b2_protocol(self, use_b2_protocol):
        """Sets the use_b2_protocol of this NativeForwardingConfigV1.


        :param use_b2_protocol: The use_b2_protocol of this NativeForwardingConfigV1.  # noqa: E501
        :type: bool
        """

        self._use_b2_protocol = use_b2_protocol

    @property
    def incoming_connect_timeout(self):
        """Gets the incoming_connect_timeout of this NativeForwardingConfigV1.  # noqa: E501


        :return: The incoming_connect_timeout of this NativeForwardingConfigV1.  # noqa: E501
        :rtype: TimeSpan
        """
        return self._incoming_connect_timeout

    @incoming_connect_timeout.setter
    def incoming_connect_timeout(self, incoming_connect_timeout):
        """Sets the incoming_connect_timeout of this NativeForwardingConfigV1.


        :param incoming_connect_timeout: The incoming_connect_timeout of this NativeForwardingConfigV1.  # noqa: E501
        :type: TimeSpan
        """

        self._incoming_connect_timeout = incoming_connect_timeout

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NativeForwardingConfigV1, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NativeForwardingConfigV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
