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


class HealthCheckResult(object):
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
        'component': 'str',
        'failure': 'Failure',
        'is_healthy': 'bool'
    }

    attribute_map = {
        'component': 'component',
        'failure': 'failure',
        'is_healthy': 'isHealthy'
    }

    def __init__(self, component=None, failure=None, is_healthy=None):  # noqa: E501
        """HealthCheckResult - a model defined in Swagger"""  # noqa: E501
        self._component = None
        self._failure = None
        self._is_healthy = None
        self.discriminator = None
        if component is not None:
            self.component = component
        if failure is not None:
            self.failure = failure
        if is_healthy is not None:
            self.is_healthy = is_healthy

    @property
    def component(self):
        """Gets the component of this HealthCheckResult.  # noqa: E501


        :return: The component of this HealthCheckResult.  # noqa: E501
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this HealthCheckResult.


        :param component: The component of this HealthCheckResult.  # noqa: E501
        :type: str
        """

        self._component = component

    @property
    def failure(self):
        """Gets the failure of this HealthCheckResult.  # noqa: E501


        :return: The failure of this HealthCheckResult.  # noqa: E501
        :rtype: Failure
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """Sets the failure of this HealthCheckResult.


        :param failure: The failure of this HealthCheckResult.  # noqa: E501
        :type: Failure
        """

        self._failure = failure

    @property
    def is_healthy(self):
        """Gets the is_healthy of this HealthCheckResult.  # noqa: E501


        :return: The is_healthy of this HealthCheckResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_healthy

    @is_healthy.setter
    def is_healthy(self, is_healthy):
        """Sets the is_healthy of this HealthCheckResult.


        :param is_healthy: The is_healthy of this HealthCheckResult.  # noqa: E501
        :type: bool
        """

        self._is_healthy = is_healthy

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
        if issubclass(HealthCheckResult, dict):
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
        if not isinstance(other, HealthCheckResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other