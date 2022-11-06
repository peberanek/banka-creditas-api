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


class InlineResponse2007(object):
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
        'current_accounts': 'list[AccountCurrent]',
        'savings_accounts': 'list[AccountSavings]',
        'term_deposit_accounts': 'list[AccountTermDeposit]'
    }

    attribute_map = {
        'current_accounts': 'currentAccounts',
        'savings_accounts': 'savingsAccounts',
        'term_deposit_accounts': 'termDepositAccounts'
    }

    def __init__(self, current_accounts=None, savings_accounts=None, term_deposit_accounts=None, _configuration=None):  # noqa: E501
        """InlineResponse2007 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._current_accounts = None
        self._savings_accounts = None
        self._term_deposit_accounts = None
        self.discriminator = None

        if current_accounts is not None:
            self.current_accounts = current_accounts
        if savings_accounts is not None:
            self.savings_accounts = savings_accounts
        if term_deposit_accounts is not None:
            self.term_deposit_accounts = term_deposit_accounts

    @property
    def current_accounts(self):
        """Gets the current_accounts of this InlineResponse2007.  # noqa: E501


        :return: The current_accounts of this InlineResponse2007.  # noqa: E501
        :rtype: list[AccountCurrent]
        """
        return self._current_accounts

    @current_accounts.setter
    def current_accounts(self, current_accounts):
        """Sets the current_accounts of this InlineResponse2007.


        :param current_accounts: The current_accounts of this InlineResponse2007.  # noqa: E501
        :type: list[AccountCurrent]
        """

        self._current_accounts = current_accounts

    @property
    def savings_accounts(self):
        """Gets the savings_accounts of this InlineResponse2007.  # noqa: E501


        :return: The savings_accounts of this InlineResponse2007.  # noqa: E501
        :rtype: list[AccountSavings]
        """
        return self._savings_accounts

    @savings_accounts.setter
    def savings_accounts(self, savings_accounts):
        """Sets the savings_accounts of this InlineResponse2007.


        :param savings_accounts: The savings_accounts of this InlineResponse2007.  # noqa: E501
        :type: list[AccountSavings]
        """

        self._savings_accounts = savings_accounts

    @property
    def term_deposit_accounts(self):
        """Gets the term_deposit_accounts of this InlineResponse2007.  # noqa: E501


        :return: The term_deposit_accounts of this InlineResponse2007.  # noqa: E501
        :rtype: list[AccountTermDeposit]
        """
        return self._term_deposit_accounts

    @term_deposit_accounts.setter
    def term_deposit_accounts(self, term_deposit_accounts):
        """Sets the term_deposit_accounts of this InlineResponse2007.


        :param term_deposit_accounts: The term_deposit_accounts of this InlineResponse2007.  # noqa: E501
        :type: list[AccountTermDeposit]
        """

        self._term_deposit_accounts = term_deposit_accounts

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
        if issubclass(InlineResponse2007, dict):
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
        if not isinstance(other, InlineResponse2007):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2007):
            return True

        return self.to_dict() != other.to_dict()
