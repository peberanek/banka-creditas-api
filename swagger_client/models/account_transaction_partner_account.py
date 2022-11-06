# coding: utf-8

"""
    Creditas OpenAPI

    This is specification of the Creditas OpenAPI. It contains definitions of Creditas banking services exposed via API accessible on the internet.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: is@creditas.cz
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class AccountTransactionPartnerAccount(object):
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
        'number': 'str',
        'bank_code': 'str',
        'bank_name': 'str',
        'partner_name': 'str'
    }

    attribute_map = {
        'number': 'number',
        'bank_code': 'bankCode',
        'bank_name': 'bankName',
        'partner_name': 'partnerName'
    }

    def __init__(self, number=None, bank_code=None, bank_name=None, partner_name=None, _configuration=None):  # noqa: E501
        """AccountTransactionPartnerAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._number = None
        self._bank_code = None
        self._bank_name = None
        self._partner_name = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if bank_code is not None:
            self.bank_code = bank_code
        if bank_name is not None:
            self.bank_name = bank_name
        if partner_name is not None:
            self.partner_name = partner_name

    @property
    def number(self):
        """Gets the number of this AccountTransactionPartnerAccount.  # noqa: E501

        The consolidated account number  # noqa: E501

        :return: The number of this AccountTransactionPartnerAccount.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this AccountTransactionPartnerAccount.

        The consolidated account number  # noqa: E501

        :param number: The number of this AccountTransactionPartnerAccount.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def bank_code(self):
        """Gets the bank_code of this AccountTransactionPartnerAccount.  # noqa: E501

        BIC (Bank Identifier Code) or the country specific bank code  # noqa: E501

        :return: The bank_code of this AccountTransactionPartnerAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this AccountTransactionPartnerAccount.

        BIC (Bank Identifier Code) or the country specific bank code  # noqa: E501

        :param bank_code: The bank_code of this AccountTransactionPartnerAccount.  # noqa: E501
        :type: str
        """

        self._bank_code = bank_code

    @property
    def bank_name(self):
        """Gets the bank_name of this AccountTransactionPartnerAccount.  # noqa: E501

        The partner's bank name  # noqa: E501

        :return: The bank_name of this AccountTransactionPartnerAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this AccountTransactionPartnerAccount.

        The partner's bank name  # noqa: E501

        :param bank_name: The bank_name of this AccountTransactionPartnerAccount.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def partner_name(self):
        """Gets the partner_name of this AccountTransactionPartnerAccount.  # noqa: E501

        The partner‘s name – a name and a surname or a company name  # noqa: E501

        :return: The partner_name of this AccountTransactionPartnerAccount.  # noqa: E501
        :rtype: str
        """
        return self._partner_name

    @partner_name.setter
    def partner_name(self, partner_name):
        """Sets the partner_name of this AccountTransactionPartnerAccount.

        The partner‘s name – a name and a surname or a company name  # noqa: E501

        :param partner_name: The partner_name of this AccountTransactionPartnerAccount.  # noqa: E501
        :type: str
        """

        self._partner_name = partner_name

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
        if issubclass(AccountTransactionPartnerAccount, dict):
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
        if not isinstance(other, AccountTransactionPartnerAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountTransactionPartnerAccount):
            return True

        return self.to_dict() != other.to_dict()
