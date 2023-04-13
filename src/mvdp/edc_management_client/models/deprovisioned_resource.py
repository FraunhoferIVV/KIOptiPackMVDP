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


class DeprovisionedResource(object):
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
        'error': 'bool',
        'error_message': 'str',
        'in_process': 'bool',
        'provisioned_resource_id': 'str'
    }

    attribute_map = {
        'error': 'error',
        'error_message': 'errorMessage',
        'in_process': 'inProcess',
        'provisioned_resource_id': 'provisionedResourceId'
    }

    def __init__(self, error=None, error_message=None, in_process=None, provisioned_resource_id=None):  # noqa: E501
        """DeprovisionedResource - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._error_message = None
        self._in_process = None
        self._provisioned_resource_id = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if error_message is not None:
            self.error_message = error_message
        if in_process is not None:
            self.in_process = in_process
        if provisioned_resource_id is not None:
            self.provisioned_resource_id = provisioned_resource_id

    @property
    def error(self):
        """Gets the error of this DeprovisionedResource.  # noqa: E501


        :return: The error of this DeprovisionedResource.  # noqa: E501
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DeprovisionedResource.


        :param error: The error of this DeprovisionedResource.  # noqa: E501
        :type: bool
        """

        self._error = error

    @property
    def error_message(self):
        """Gets the error_message of this DeprovisionedResource.  # noqa: E501


        :return: The error_message of this DeprovisionedResource.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this DeprovisionedResource.


        :param error_message: The error_message of this DeprovisionedResource.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def in_process(self):
        """Gets the in_process of this DeprovisionedResource.  # noqa: E501


        :return: The in_process of this DeprovisionedResource.  # noqa: E501
        :rtype: bool
        """
        return self._in_process

    @in_process.setter
    def in_process(self, in_process):
        """Sets the in_process of this DeprovisionedResource.


        :param in_process: The in_process of this DeprovisionedResource.  # noqa: E501
        :type: bool
        """

        self._in_process = in_process

    @property
    def provisioned_resource_id(self):
        """Gets the provisioned_resource_id of this DeprovisionedResource.  # noqa: E501


        :return: The provisioned_resource_id of this DeprovisionedResource.  # noqa: E501
        :rtype: str
        """
        return self._provisioned_resource_id

    @provisioned_resource_id.setter
    def provisioned_resource_id(self, provisioned_resource_id):
        """Sets the provisioned_resource_id of this DeprovisionedResource.


        :param provisioned_resource_id: The provisioned_resource_id of this DeprovisionedResource.  # noqa: E501
        :type: str
        """

        self._provisioned_resource_id = provisioned_resource_id

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
        if issubclass(DeprovisionedResource, dict):
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
        if not isinstance(other, DeprovisionedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
