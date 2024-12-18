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

class MHeardMonoportDetails(object):
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
        'last_heard': 'datetime',
        'packets': 'int'
    }

    attribute_map = {
        'last_heard': 'lastHeard',
        'packets': 'packets'
    }

    def __init__(self, last_heard=None, packets=None):  # noqa: E501
        """MHeardMonoportDetails - a model defined in Swagger"""  # noqa: E501
        self._last_heard = None
        self._packets = None
        self.discriminator = None
        if last_heard is not None:
            self.last_heard = last_heard
        if packets is not None:
            self.packets = packets

    @property
    def last_heard(self):
        """Gets the last_heard of this MHeardMonoportDetails.  # noqa: E501


        :return: The last_heard of this MHeardMonoportDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._last_heard

    @last_heard.setter
    def last_heard(self, last_heard):
        """Sets the last_heard of this MHeardMonoportDetails.


        :param last_heard: The last_heard of this MHeardMonoportDetails.  # noqa: E501
        :type: datetime
        """

        self._last_heard = last_heard

    @property
    def packets(self):
        """Gets the packets of this MHeardMonoportDetails.  # noqa: E501


        :return: The packets of this MHeardMonoportDetails.  # noqa: E501
        :rtype: int
        """
        return self._packets

    @packets.setter
    def packets(self, packets):
        """Sets the packets of this MHeardMonoportDetails.


        :param packets: The packets of this MHeardMonoportDetails.  # noqa: E501
        :type: int
        """

        self._packets = packets

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
        if issubclass(MHeardMonoportDetails, dict):
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
        if not isinstance(other, MHeardMonoportDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
