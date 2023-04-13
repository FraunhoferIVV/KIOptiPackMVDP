# coding: utf-8

"""
    management-api

    REST API documentation for the management-api  # noqa: E501

    OpenAPI spec version: 0.0.1-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class DataPlaneInstance(object):
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
        'allowed_dest_types': 'list[str]',
        'allowed_source_types': 'list[str]',
        'id': 'str',
        'last_active': 'int',
        'properties': 'dict(str, object)',
        'turn_count': 'int',
        'url': 'str'
    }

    attribute_map = {
        'allowed_dest_types': 'allowedDestTypes',
        'allowed_source_types': 'allowedSourceTypes',
        'id': 'id',
        'last_active': 'lastActive',
        'properties': 'properties',
        'turn_count': 'turnCount',
        'url': 'url'
    }

    def __init__(self, allowed_dest_types=None, allowed_source_types=None, id=None, last_active=None, properties=None,
                 turn_count=None, url=None):  # noqa: E501
        """DataPlaneInstance - a model defined in Swagger"""  # noqa: E501
        self._allowed_dest_types = None
        self._allowed_source_types = None
        self._id = None
        self._last_active = None
        self._properties = None
        self._turn_count = None
        self._url = None
        self.discriminator = None
        if allowed_dest_types is not None:
            self.allowed_dest_types = allowed_dest_types
        if allowed_source_types is not None:
            self.allowed_source_types = allowed_source_types
        if id is not None:
            self.id = id
        if last_active is not None:
            self.last_active = last_active
        if properties is not None:
            self.properties = properties
        if turn_count is not None:
            self.turn_count = turn_count
        if url is not None:
            self.url = url

    @property
    def allowed_dest_types(self):
        """Gets the allowed_dest_types of this DataPlaneInstance.  # noqa: E501


        :return: The allowed_dest_types of this DataPlaneInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_dest_types

    @allowed_dest_types.setter
    def allowed_dest_types(self, allowed_dest_types):
        """Sets the allowed_dest_types of this DataPlaneInstance.


        :param allowed_dest_types: The allowed_dest_types of this DataPlaneInstance.  # noqa: E501
        :type: list[str]
        """

        self._allowed_dest_types = allowed_dest_types

    @property
    def allowed_source_types(self):
        """Gets the allowed_source_types of this DataPlaneInstance.  # noqa: E501


        :return: The allowed_source_types of this DataPlaneInstance.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_source_types

    @allowed_source_types.setter
    def allowed_source_types(self, allowed_source_types):
        """Sets the allowed_source_types of this DataPlaneInstance.


        :param allowed_source_types: The allowed_source_types of this DataPlaneInstance.  # noqa: E501
        :type: list[str]
        """

        self._allowed_source_types = allowed_source_types

    @property
    def id(self):
        """Gets the id of this DataPlaneInstance.  # noqa: E501


        :return: The id of this DataPlaneInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataPlaneInstance.


        :param id: The id of this DataPlaneInstance.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_active(self):
        """Gets the last_active of this DataPlaneInstance.  # noqa: E501


        :return: The last_active of this DataPlaneInstance.  # noqa: E501
        :rtype: int
        """
        return self._last_active

    @last_active.setter
    def last_active(self, last_active):
        """Sets the last_active of this DataPlaneInstance.


        :param last_active: The last_active of this DataPlaneInstance.  # noqa: E501
        :type: int
        """

        self._last_active = last_active

    @property
    def properties(self):
        """Gets the properties of this DataPlaneInstance.  # noqa: E501


        :return: The properties of this DataPlaneInstance.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this DataPlaneInstance.


        :param properties: The properties of this DataPlaneInstance.  # noqa: E501
        :type: dict(str, object)
        """

        self._properties = properties

    @property
    def turn_count(self):
        """Gets the turn_count of this DataPlaneInstance.  # noqa: E501


        :return: The turn_count of this DataPlaneInstance.  # noqa: E501
        :rtype: int
        """
        return self._turn_count

    @turn_count.setter
    def turn_count(self, turn_count):
        """Sets the turn_count of this DataPlaneInstance.


        :param turn_count: The turn_count of this DataPlaneInstance.  # noqa: E501
        :type: int
        """

        self._turn_count = turn_count

    @property
    def url(self):
        """Gets the url of this DataPlaneInstance.  # noqa: E501


        :return: The url of this DataPlaneInstance.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DataPlaneInstance.


        :param url: The url of this DataPlaneInstance.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(DataPlaneInstance, dict):
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
        if not isinstance(other, DataPlaneInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
