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


class QuerySpecDto(object):
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
        'filter': 'str',
        'filter_expression': 'list[CriterionDto]',
        'limit': 'int',
        'offset': 'int',
        'sort_field': 'str',
        'sort_order': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'filter_expression': 'filterExpression',
        'limit': 'limit',
        'offset': 'offset',
        'sort_field': 'sortField',
        'sort_order': 'sortOrder'
    }

    def __init__(self, filter=None, filter_expression=None, limit=None, offset=None, sort_field=None,
                 sort_order=None):  # noqa: E501
        """QuerySpecDto - a model defined in Swagger"""  # noqa: E501
        self._filter = None
        self._filter_expression = None
        self._limit = None
        self._offset = None
        self._sort_field = None
        self._sort_order = None
        self.discriminator = None
        if filter is not None:
            self.filter = filter
        if filter_expression is not None:
            self.filter_expression = filter_expression
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def filter(self):
        """Gets the filter of this QuerySpecDto.  # noqa: E501


        :return: The filter of this QuerySpecDto.  # noqa: E501
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this QuerySpecDto.


        :param filter: The filter of this QuerySpecDto.  # noqa: E501
        :type: str
        """

        self._filter = filter

    @property
    def filter_expression(self):
        """Gets the filter_expression of this QuerySpecDto.  # noqa: E501


        :return: The filter_expression of this QuerySpecDto.  # noqa: E501
        :rtype: list[CriterionDto]
        """
        return self._filter_expression

    @filter_expression.setter
    def filter_expression(self, filter_expression):
        """Sets the filter_expression of this QuerySpecDto.


        :param filter_expression: The filter_expression of this QuerySpecDto.  # noqa: E501
        :type: list[CriterionDto]
        """

        self._filter_expression = filter_expression

    @property
    def limit(self):
        """Gets the limit of this QuerySpecDto.  # noqa: E501


        :return: The limit of this QuerySpecDto.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QuerySpecDto.


        :param limit: The limit of this QuerySpecDto.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this QuerySpecDto.  # noqa: E501


        :return: The offset of this QuerySpecDto.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QuerySpecDto.


        :param offset: The offset of this QuerySpecDto.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def sort_field(self):
        """Gets the sort_field of this QuerySpecDto.  # noqa: E501


        :return: The sort_field of this QuerySpecDto.  # noqa: E501
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this QuerySpecDto.


        :param sort_field: The sort_field of this QuerySpecDto.  # noqa: E501
        :type: str
        """

        self._sort_field = sort_field

    @property
    def sort_order(self):
        """Gets the sort_order of this QuerySpecDto.  # noqa: E501


        :return: The sort_order of this QuerySpecDto.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this QuerySpecDto.


        :param sort_order: The sort_order of this QuerySpecDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASC", "DESC"]  # noqa: E501
        if sort_order not in allowed_values:
            raise ValueError(
                "Invalid value for `sort_order` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_order, allowed_values)
            )

        self._sort_order = sort_order

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
        if issubclass(QuerySpecDto, dict):
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
        if not isinstance(other, QuerySpecDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other