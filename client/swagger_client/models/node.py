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

class Node(object):
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
        'call': 'str',
        'alias': 'str',
        'routes': 'list[BpqRoute]'
    }

    attribute_map = {
        'call': 'call',
        'alias': 'alias',
        'routes': 'routes'
    }

    def __init__(self, call=None, alias=None, routes=None):  # noqa: E501
        """Node - a model defined in Swagger"""  # noqa: E501
        self._call = None
        self._alias = None
        self._routes = None
        self.discriminator = None
        if call is not None:
            self.call = call
        if alias is not None:
            self.alias = alias
        if routes is not None:
            self.routes = routes

    @property
    def call(self):
        """Gets the call of this Node.  # noqa: E501


        :return: The call of this Node.  # noqa: E501
        :rtype: str
        """
        return self._call

    @call.setter
    def call(self, call):
        """Sets the call of this Node.


        :param call: The call of this Node.  # noqa: E501
        :type: str
        """

        self._call = call

    @property
    def alias(self):
        """Gets the alias of this Node.  # noqa: E501


        :return: The alias of this Node.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this Node.


        :param alias: The alias of this Node.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def routes(self):
        """Gets the routes of this Node.  # noqa: E501


        :return: The routes of this Node.  # noqa: E501
        :rtype: list[BpqRoute]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        """Sets the routes of this Node.


        :param routes: The routes of this Node.  # noqa: E501
        :type: list[BpqRoute]
        """

        self._routes = routes

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
        if issubclass(Node, dict):
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
        if not isinstance(other, Node):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
