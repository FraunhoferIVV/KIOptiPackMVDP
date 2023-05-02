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


class PolicyDefinitionResponseDto(object):
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
        'created_at': 'int',
        'id': 'str',
        'policy': 'Policy'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'id': 'id',
        'policy': 'policy'
    }

    def __init__(self, created_at=None, id=None, policy=None):  # noqa: E501
        """PolicyDefinitionResponseDto - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._id = None
        self._policy = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        self.policy = policy

    @property
    def created_at(self):
        """Gets the created_at of this PolicyDefinitionResponseDto.  # noqa: E501


        :return: The created_at of this PolicyDefinitionResponseDto.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PolicyDefinitionResponseDto.


        :param created_at: The created_at of this PolicyDefinitionResponseDto.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this PolicyDefinitionResponseDto.  # noqa: E501


        :return: The id of this PolicyDefinitionResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyDefinitionResponseDto.


        :param id: The id of this PolicyDefinitionResponseDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def policy(self):
        """Gets the policy of this PolicyDefinitionResponseDto.  # noqa: E501


        :return: The policy of this PolicyDefinitionResponseDto.  # noqa: E501
        :rtype: Policy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this PolicyDefinitionResponseDto.


        :param policy: The policy of this PolicyDefinitionResponseDto.  # noqa: E501
        :type: Policy
        """
        if policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

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
        if issubclass(PolicyDefinitionResponseDto, dict):
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
        if not isinstance(other, PolicyDefinitionResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other