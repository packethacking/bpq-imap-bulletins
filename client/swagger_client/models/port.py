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

class Port(object):
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
        'id': 'str',
        'driver': 'str',
        'number': 'int',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'driver': 'driver',
        'number': 'number',
        'state': 'state'
    }

    def __init__(self, id=None, driver=None, number=None, state=None):  # noqa: E501
        """Port - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._driver = None
        self._number = None
        self._state = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if driver is not None:
            self.driver = driver
        if number is not None:
            self.number = number
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this Port.  # noqa: E501


        :return: The id of this Port.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Port.


        :param id: The id of this Port.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def driver(self):
        """Gets the driver of this Port.  # noqa: E501


        :return: The driver of this Port.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this Port.


        :param driver: The driver of this Port.  # noqa: E501
        :type: str
        """

        self._driver = driver

    @property
    def number(self):
        """Gets the number of this Port.  # noqa: E501


        :return: The number of this Port.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Port.


        :param number: The number of this Port.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def state(self):
        """Gets the state of this Port.  # noqa: E501


        :return: The state of this Port.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Port.


        :param state: The state of this Port.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(Port, dict):
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
        if not isinstance(other, Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
