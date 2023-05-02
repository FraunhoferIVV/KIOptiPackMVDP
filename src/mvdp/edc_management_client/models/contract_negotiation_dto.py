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


class ContractNegotiationDto(object):
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
        'contract_agreement_id': 'str',
        'counter_party_address': 'str',
        'created_at': 'int',
        'error_detail': 'str',
        'id': 'str',
        'protocol': 'str',
        'state': 'str',
        'type': 'str',
        'updated_at': 'int'
    }

    attribute_map = {
        'contract_agreement_id': 'contractAgreementId',
        'counter_party_address': 'counterPartyAddress',
        'created_at': 'createdAt',
        'error_detail': 'errorDetail',
        'id': 'id',
        'protocol': 'protocol',
        'state': 'state',
        'type': 'type',
        'updated_at': 'updatedAt'
    }

    def __init__(self, contract_agreement_id=None, counter_party_address=None, created_at=None, error_detail=None,
                 id=None, protocol=None, state=None, type=None, updated_at=None):  # noqa: E501
        """ContractNegotiationDto - a model defined in Swagger"""  # noqa: E501
        self._contract_agreement_id = None
        self._counter_party_address = None
        self._created_at = None
        self._error_detail = None
        self._id = None
        self._protocol = None
        self._state = None
        self._type = None
        self._updated_at = None
        self.discriminator = None
        if contract_agreement_id is not None:
            self.contract_agreement_id = contract_agreement_id
        if counter_party_address is not None:
            self.counter_party_address = counter_party_address
        if created_at is not None:
            self.created_at = created_at
        if error_detail is not None:
            self.error_detail = error_detail
        if id is not None:
            self.id = id
        if protocol is not None:
            self.protocol = protocol
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def contract_agreement_id(self):
        """Gets the contract_agreement_id of this ContractNegotiationDto.  # noqa: E501


        :return: The contract_agreement_id of this ContractNegotiationDto.  # noqa: E501
        :rtype: str
        """
        return self._contract_agreement_id

    @contract_agreement_id.setter
    def contract_agreement_id(self, contract_agreement_id):
        """Sets the contract_agreement_id of this ContractNegotiationDto.


        :param contract_agreement_id: The contract_agreement_id of this ContractNegotiationDto.  # noqa: E501
        :type: str
        """

        self._contract_agreement_id = contract_agreement_id

    @property
    def counter_party_address(self):
        """Gets the counter_party_address of this ContractNegotiationDto.  # noqa: E501


        :return: The counter_party_address of this ContractNegotiationDto.  # noqa: E501
        :rtype: str
        """
        return self._counter_party_address

    @counter_party_address.setter
    def counter_party_address(self, counter_party_address):
        """Sets the counter_party_address of this ContractNegotiationDto.


        :param counter_party_address: The counter_party_address of this ContractNegotiationDto.  # noqa: E501
        :type: str
        """

        self._counter_party_address = counter_party_address

    @property
    def created_at(self):
        """Gets the created_at of this ContractNegotiationDto.  # noqa: E501


        :return: The created_at of this ContractNegotiationDto.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ContractNegotiationDto.


        :param created_at: The created_at of this ContractNegotiationDto.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def error_detail(self):
        """Gets the error_detail of this ContractNegotiationDto.  # noqa: E501


        :return: The error_detail of this ContractNegotiationDto.  # noqa: E501
        :rtype: str
        """
        return self._error_detail

    @error_detail.setter
    def error_detail(self, error_detail):
        """Sets the error_detail of this ContractNegotiationDto.


        :param error_detail: The error_detail of this ContractNegotiationDto.  # noqa: E501
        :type: str
        """

        self._error_detail = error_detail

    @property
    def id(self):
        """Gets the id of this ContractNegotiationDto.  # noqa: E501


        :return: The id of this ContractNegotiationDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContractNegotiationDto.


        :param id: The id of this ContractNegotiationDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def protocol(self):
        """Gets the protocol of this ContractNegotiationDto.  # noqa: E501


        :return: The protocol of this ContractNegotiationDto.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ContractNegotiationDto.


        :param protocol: The protocol of this ContractNegotiationDto.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def state(self):
        """Gets the state of this ContractNegotiationDto.  # noqa: E501


        :return: The state of this ContractNegotiationDto.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ContractNegotiationDto.


        :param state: The state of this ContractNegotiationDto.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def type(self):
        """Gets the type of this ContractNegotiationDto.  # noqa: E501


        :return: The type of this ContractNegotiationDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ContractNegotiationDto.


        :param type: The type of this ContractNegotiationDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONSUMER", "PROVIDER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this ContractNegotiationDto.  # noqa: E501


        :return: The updated_at of this ContractNegotiationDto.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ContractNegotiationDto.


        :param updated_at: The updated_at of this ContractNegotiationDto.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

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
        if issubclass(ContractNegotiationDto, dict):
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
        if not isinstance(other, ContractNegotiationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other