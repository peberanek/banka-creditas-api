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


class AccountSavings(object):
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
        'account_id': 'str',
        'bban': 'str',
        'bank_code': 'str',
        'iban': 'str',
        'bic': 'str',
        'currency': 'str',
        'country': 'str',
        'status': 'str',
        'name': 'str',
        'alias': 'str',
        'product_i18_n': 'str',
        'current_balance': 'str',
        'available_balance': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'bban': 'bban',
        'bank_code': 'bankCode',
        'iban': 'iban',
        'bic': 'bic',
        'currency': 'currency',
        'country': 'country',
        'status': 'status',
        'name': 'name',
        'alias': 'alias',
        'product_i18_n': 'productI18N',
        'current_balance': 'currentBalance',
        'available_balance': 'availableBalance'
    }

    def __init__(self, account_id=None, bban=None, bank_code=None, iban=None, bic=None, currency=None, country=None, status=None, name=None, alias=None, product_i18_n=None, current_balance=None, available_balance=None, _configuration=None):  # noqa: E501
        """AccountSavings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._bban = None
        self._bank_code = None
        self._iban = None
        self._bic = None
        self._currency = None
        self._country = None
        self._status = None
        self._name = None
        self._alias = None
        self._product_i18_n = None
        self._current_balance = None
        self._available_balance = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if bban is not None:
            self.bban = bban
        if bank_code is not None:
            self.bank_code = bank_code
        if iban is not None:
            self.iban = iban
        if bic is not None:
            self.bic = bic
        if currency is not None:
            self.currency = currency
        if country is not None:
            self.country = country
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if alias is not None:
            self.alias = alias
        if product_i18_n is not None:
            self.product_i18_n = product_i18_n
        if current_balance is not None:
            self.current_balance = current_balance
        if available_balance is not None:
            self.available_balance = available_balance

    @property
    def account_id(self):
        """Gets the account_id of this AccountSavings.  # noqa: E501

        The unique identifier for the account  # noqa: E501

        :return: The account_id of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountSavings.

        The unique identifier for the account  # noqa: E501

        :param account_id: The account_id of this AccountSavings.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                account_id is not None and len(account_id) > 40):
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `40`")  # noqa: E501

        self._account_id = account_id

    @property
    def bban(self):
        """Gets the bban of this AccountSavings.  # noqa: E501

        BBAN (Basic Bank Account Number) The country-specific account number  # noqa: E501

        :return: The bban of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._bban

    @bban.setter
    def bban(self, bban):
        """Sets the bban of this AccountSavings.

        BBAN (Basic Bank Account Number) The country-specific account number  # noqa: E501

        :param bban: The bban of this AccountSavings.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bban is not None and len(bban) > 42):
            raise ValueError("Invalid value for `bban`, length must be less than or equal to `42`")  # noqa: E501

        self._bban = bban

    @property
    def bank_code(self):
        """Gets the bank_code of this AccountSavings.  # noqa: E501

        The country specific bank code  # noqa: E501

        :return: The bank_code of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._bank_code

    @bank_code.setter
    def bank_code(self, bank_code):
        """Sets the bank_code of this AccountSavings.

        The country specific bank code  # noqa: E501

        :param bank_code: The bank_code of this AccountSavings.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bank_code is not None and len(bank_code) > 4):
            raise ValueError("Invalid value for `bank_code`, length must be less than or equal to `4`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bank_code is not None and len(bank_code) < 4):
            raise ValueError("Invalid value for `bank_code`, length must be greater than or equal to `4`")  # noqa: E501

        self._bank_code = bank_code

    @property
    def iban(self):
        """Gets the iban of this AccountSavings.  # noqa: E501

        IBAN (International Bank Account Number)  # noqa: E501

        :return: The iban of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this AccountSavings.

        IBAN (International Bank Account Number)  # noqa: E501

        :param iban: The iban of this AccountSavings.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                iban is not None and len(iban) > 42):
            raise ValueError("Invalid value for `iban`, length must be less than or equal to `42`")  # noqa: E501

        self._iban = iban

    @property
    def bic(self):
        """Gets the bic of this AccountSavings.  # noqa: E501

        BIC (Business Identification Code) - International unique identifier for the bank  # noqa: E501

        :return: The bic of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this AccountSavings.

        BIC (Business Identification Code) - International unique identifier for the bank  # noqa: E501

        :param bic: The bic of this AccountSavings.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                bic is not None and len(bic) > 11):
            raise ValueError("Invalid value for `bic`, length must be less than or equal to `11`")  # noqa: E501
        if (self._configuration.client_side_validation and
                bic is not None and len(bic) < 8):
            raise ValueError("Invalid value for `bic`, length must be greater than or equal to `8`")  # noqa: E501

        self._bic = bic

    @property
    def currency(self):
        """Gets the currency of this AccountSavings.  # noqa: E501

        The account's currency code in ISO 4217 format (CZK, EUR, USD, ...)  # noqa: E501

        :return: The currency of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AccountSavings.

        The account's currency code in ISO 4217 format (CZK, EUR, USD, ...)  # noqa: E501

        :param currency: The currency of this AccountSavings.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                currency is not None and len(currency) > 3):
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")  # noqa: E501
        if (self._configuration.client_side_validation and
                currency is not None and len(currency) < 3):
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._currency = currency

    @property
    def country(self):
        """Gets the country of this AccountSavings.  # noqa: E501

        The country code of the account's origin in ISO 3166-1 alpha-3 format (CZE, SVK, ...)  # noqa: E501

        :return: The country of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AccountSavings.

        The country code of the account's origin in ISO 3166-1 alpha-3 format (CZE, SVK, ...)  # noqa: E501

        :param country: The country of this AccountSavings.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                country is not None and len(country) > 3):
            raise ValueError("Invalid value for `country`, length must be less than or equal to `3`")  # noqa: E501
        if (self._configuration.client_side_validation and
                country is not None and len(country) < 3):
            raise ValueError("Invalid value for `country`, length must be greater than or equal to `3`")  # noqa: E501

        self._country = country

    @property
    def status(self):
        """Gets the status of this AccountSavings.  # noqa: E501

        The status of the account  # noqa: E501

        :return: The status of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AccountSavings.

        The status of the account  # noqa: E501

        :param status: The status of this AccountSavings.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "INACTIVE", "CLOSED", "TO_BE_CLOSED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def name(self):
        """Gets the name of this AccountSavings.  # noqa: E501

        The name (description) for the account (typically the name of the account's owner)  # noqa: E501

        :return: The name of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountSavings.

        The name (description) for the account (typically the name of the account's owner)  # noqa: E501

        :param name: The name of this AccountSavings.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def alias(self):
        """Gets the alias of this AccountSavings.  # noqa: E501

        The consumer preferred account name  # noqa: E501

        :return: The alias of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this AccountSavings.

        The consumer preferred account name  # noqa: E501

        :param alias: The alias of this AccountSavings.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def product_i18_n(self):
        """Gets the product_i18_n of this AccountSavings.  # noqa: E501

        The localized bank account product description (business product name)  # noqa: E501

        :return: The product_i18_n of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._product_i18_n

    @product_i18_n.setter
    def product_i18_n(self, product_i18_n):
        """Sets the product_i18_n of this AccountSavings.

        The localized bank account product description (business product name)  # noqa: E501

        :param product_i18_n: The product_i18_n of this AccountSavings.  # noqa: E501
        :type: str
        """

        self._product_i18_n = product_i18_n

    @property
    def current_balance(self):
        """Gets the current_balance of this AccountSavings.  # noqa: E501

        The current account balance (may not include transactions yet to be posted to the account often as of previous business day)  # noqa: E501

        :return: The current_balance of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._current_balance

    @current_balance.setter
    def current_balance(self, current_balance):
        """Sets the current_balance of this AccountSavings.

        The current account balance (may not include transactions yet to be posted to the account often as of previous business day)  # noqa: E501

        :param current_balance: The current_balance of this AccountSavings.  # noqa: E501
        :type: str
        """

        self._current_balance = current_balance

    @property
    def available_balance(self):
        """Gets the available_balance of this AccountSavings.  # noqa: E501

        The available balance in the account (may include pending transactions and overdraft limit)  # noqa: E501

        :return: The available_balance of this AccountSavings.  # noqa: E501
        :rtype: str
        """
        return self._available_balance

    @available_balance.setter
    def available_balance(self, available_balance):
        """Sets the available_balance of this AccountSavings.

        The available balance in the account (may include pending transactions and overdraft limit)  # noqa: E501

        :param available_balance: The available_balance of this AccountSavings.  # noqa: E501
        :type: str
        """

        self._available_balance = available_balance

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
        if issubclass(AccountSavings, dict):
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
        if not isinstance(other, AccountSavings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountSavings):
            return True

        return self.to_dict() != other.to_dict()