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


class AccountTransaction(object):
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
        'transaction_id': 'str',
        'category': 'str',
        'type': 'str',
        'code': 'str',
        'code_i18_n': 'str',
        'partner_account': 'AccountTransactionPartnerAccount',
        'amount': 'Money',
        'effective_date': 'date',
        'card_authorization_date': 'date',
        'variable_symbol': 'str',
        'specific_symbol': 'str',
        'constant_symbol': 'str',
        'payers_reference': 'str',
        'remittance_info': 'str',
        'user_note': 'str',
        'balance': 'Money',
        'payment_order_id': 'str',
        'bulk_payment_order_id': 'str'
    }

    attribute_map = {
        'transaction_id': 'transactionId',
        'category': 'category',
        'type': 'type',
        'code': 'code',
        'code_i18_n': 'codeI18N',
        'partner_account': 'partnerAccount',
        'amount': 'amount',
        'effective_date': 'effectiveDate',
        'card_authorization_date': 'cardAuthorizationDate',
        'variable_symbol': 'variableSymbol',
        'specific_symbol': 'specificSymbol',
        'constant_symbol': 'constantSymbol',
        'payers_reference': 'payersReference',
        'remittance_info': 'remittanceInfo',
        'user_note': 'userNote',
        'balance': 'balance',
        'payment_order_id': 'paymentOrderId',
        'bulk_payment_order_id': 'bulkPaymentOrderId'
    }

    def __init__(self, transaction_id=None, category=None, type=None, code=None, code_i18_n=None, partner_account=None, amount=None, effective_date=None, card_authorization_date=None, variable_symbol=None, specific_symbol=None, constant_symbol=None, payers_reference=None, remittance_info=None, user_note=None, balance=None, payment_order_id=None, bulk_payment_order_id=None, _configuration=None):  # noqa: E501
        """AccountTransaction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_id = None
        self._category = None
        self._type = None
        self._code = None
        self._code_i18_n = None
        self._partner_account = None
        self._amount = None
        self._effective_date = None
        self._card_authorization_date = None
        self._variable_symbol = None
        self._specific_symbol = None
        self._constant_symbol = None
        self._payers_reference = None
        self._remittance_info = None
        self._user_note = None
        self._balance = None
        self._payment_order_id = None
        self._bulk_payment_order_id = None
        self.discriminator = None

        self.transaction_id = transaction_id
        self.category = category
        self.type = type
        self.code = code
        if code_i18_n is not None:
            self.code_i18_n = code_i18_n
        if partner_account is not None:
            self.partner_account = partner_account
        self.amount = amount
        self.effective_date = effective_date
        if card_authorization_date is not None:
            self.card_authorization_date = card_authorization_date
        if variable_symbol is not None:
            self.variable_symbol = variable_symbol
        if specific_symbol is not None:
            self.specific_symbol = specific_symbol
        if constant_symbol is not None:
            self.constant_symbol = constant_symbol
        if payers_reference is not None:
            self.payers_reference = payers_reference
        if remittance_info is not None:
            self.remittance_info = remittance_info
        if user_note is not None:
            self.user_note = user_note
        if balance is not None:
            self.balance = balance
        if payment_order_id is not None:
            self.payment_order_id = payment_order_id
        if bulk_payment_order_id is not None:
            self.bulk_payment_order_id = bulk_payment_order_id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this AccountTransaction.  # noqa: E501

        The unique identifier for the transaction record  # noqa: E501

        :return: The transaction_id of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this AccountTransaction.

        The unique identifier for the transaction record  # noqa: E501

        :param transaction_id: The transaction_id of this AccountTransaction.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

    @property
    def category(self):
        """Gets the category of this AccountTransaction.  # noqa: E501

        The transaction category  # noqa: E501

        :return: The category of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AccountTransaction.

        The transaction category  # noqa: E501

        :param category: The category of this AccountTransaction.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        allowed_values = ["DOMESTIC", "FOREIGN", "CARD", "OTHER"]  # noqa: E501
        if (self._configuration.client_side_validation and
                category not in allowed_values):
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def type(self):
        """Gets the type of this AccountTransaction.  # noqa: E501

        The transaction type  # noqa: E501

        :return: The type of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountTransaction.

        The transaction type  # noqa: E501

        :param type: The type of this AccountTransaction.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["CREDIT", "DEBIT"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def code(self):
        """Gets the code of this AccountTransaction.  # noqa: E501

        The transaction code  # noqa: E501

        :return: The code of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AccountTransaction.

        The transaction code  # noqa: E501

        :param code: The code of this AccountTransaction.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def code_i18_n(self):
        """Gets the code_i18_n of this AccountTransaction.  # noqa: E501

        The transaction code localized description  # noqa: E501

        :return: The code_i18_n of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._code_i18_n

    @code_i18_n.setter
    def code_i18_n(self, code_i18_n):
        """Sets the code_i18_n of this AccountTransaction.

        The transaction code localized description  # noqa: E501

        :param code_i18_n: The code_i18_n of this AccountTransaction.  # noqa: E501
        :type: str
        """

        self._code_i18_n = code_i18_n

    @property
    def partner_account(self):
        """Gets the partner_account of this AccountTransaction.  # noqa: E501


        :return: The partner_account of this AccountTransaction.  # noqa: E501
        :rtype: AccountTransactionPartnerAccount
        """
        return self._partner_account

    @partner_account.setter
    def partner_account(self, partner_account):
        """Sets the partner_account of this AccountTransaction.


        :param partner_account: The partner_account of this AccountTransaction.  # noqa: E501
        :type: AccountTransactionPartnerAccount
        """

        self._partner_account = partner_account

    @property
    def amount(self):
        """Gets the amount of this AccountTransaction.  # noqa: E501


        :return: The amount of this AccountTransaction.  # noqa: E501
        :rtype: Money
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AccountTransaction.


        :param amount: The amount of this AccountTransaction.  # noqa: E501
        :type: Money
        """
        if self._configuration.client_side_validation and amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def effective_date(self):
        """Gets the effective_date of this AccountTransaction.  # noqa: E501

        The transaction effective/value date  # noqa: E501

        :return: The effective_date of this AccountTransaction.  # noqa: E501
        :rtype: date
        """
        return self._effective_date

    @effective_date.setter
    def effective_date(self, effective_date):
        """Sets the effective_date of this AccountTransaction.

        The transaction effective/value date  # noqa: E501

        :param effective_date: The effective_date of this AccountTransaction.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and effective_date is None:
            raise ValueError("Invalid value for `effective_date`, must not be `None`")  # noqa: E501

        self._effective_date = effective_date

    @property
    def card_authorization_date(self):
        """Gets the card_authorization_date of this AccountTransaction.  # noqa: E501

        The date of the card transaction authorization  # noqa: E501

        :return: The card_authorization_date of this AccountTransaction.  # noqa: E501
        :rtype: date
        """
        return self._card_authorization_date

    @card_authorization_date.setter
    def card_authorization_date(self, card_authorization_date):
        """Sets the card_authorization_date of this AccountTransaction.

        The date of the card transaction authorization  # noqa: E501

        :param card_authorization_date: The card_authorization_date of this AccountTransaction.  # noqa: E501
        :type: date
        """

        self._card_authorization_date = card_authorization_date

    @property
    def variable_symbol(self):
        """Gets the variable_symbol of this AccountTransaction.  # noqa: E501

        The variable symbol  # noqa: E501

        :return: The variable_symbol of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._variable_symbol

    @variable_symbol.setter
    def variable_symbol(self, variable_symbol):
        """Sets the variable_symbol of this AccountTransaction.

        The variable symbol  # noqa: E501

        :param variable_symbol: The variable_symbol of this AccountTransaction.  # noqa: E501
        :type: str
        """

        self._variable_symbol = variable_symbol

    @property
    def specific_symbol(self):
        """Gets the specific_symbol of this AccountTransaction.  # noqa: E501

        The specific symbol  # noqa: E501

        :return: The specific_symbol of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._specific_symbol

    @specific_symbol.setter
    def specific_symbol(self, specific_symbol):
        """Sets the specific_symbol of this AccountTransaction.

        The specific symbol  # noqa: E501

        :param specific_symbol: The specific_symbol of this AccountTransaction.  # noqa: E501
        :type: str
        """

        self._specific_symbol = specific_symbol

    @property
    def constant_symbol(self):
        """Gets the constant_symbol of this AccountTransaction.  # noqa: E501

        The constant symbol  # noqa: E501

        :return: The constant_symbol of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._constant_symbol

    @constant_symbol.setter
    def constant_symbol(self, constant_symbol):
        """Sets the constant_symbol of this AccountTransaction.

        The constant symbol  # noqa: E501

        :param constant_symbol: The constant_symbol of this AccountTransaction.  # noqa: E501
        :type: str
        """

        self._constant_symbol = constant_symbol

    @property
    def payers_reference(self):
        """Gets the payers_reference of this AccountTransaction.  # noqa: E501

        Information allowing the beneficiary to identify the payment  # noqa: E501

        :return: The payers_reference of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payers_reference

    @payers_reference.setter
    def payers_reference(self, payers_reference):
        """Sets the payers_reference of this AccountTransaction.

        Information allowing the beneficiary to identify the payment  # noqa: E501

        :param payers_reference: The payers_reference of this AccountTransaction.  # noqa: E501
        :type: str
        """

        self._payers_reference = payers_reference

    @property
    def remittance_info(self):
        """Gets the remittance_info of this AccountTransaction.  # noqa: E501

        The remittance information - additional information for the payment beneficiary  # noqa: E501

        :return: The remittance_info of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._remittance_info

    @remittance_info.setter
    def remittance_info(self, remittance_info):
        """Sets the remittance_info of this AccountTransaction.

        The remittance information - additional information for the payment beneficiary  # noqa: E501

        :param remittance_info: The remittance_info of this AccountTransaction.  # noqa: E501
        :type: str
        """

        self._remittance_info = remittance_info

    @property
    def user_note(self):
        """Gets the user_note of this AccountTransaction.  # noqa: E501

        The user defined note  # noqa: E501

        :return: The user_note of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._user_note

    @user_note.setter
    def user_note(self, user_note):
        """Sets the user_note of this AccountTransaction.

        The user defined note  # noqa: E501

        :param user_note: The user_note of this AccountTransaction.  # noqa: E501
        :type: str
        """

        self._user_note = user_note

    @property
    def balance(self):
        """Gets the balance of this AccountTransaction.  # noqa: E501


        :return: The balance of this AccountTransaction.  # noqa: E501
        :rtype: Money
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this AccountTransaction.


        :param balance: The balance of this AccountTransaction.  # noqa: E501
        :type: Money
        """

        self._balance = balance

    @property
    def payment_order_id(self):
        """Gets the payment_order_id of this AccountTransaction.  # noqa: E501

        The unique identifier for the payment order the transaction is associated with  # noqa: E501

        :return: The payment_order_id of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._payment_order_id

    @payment_order_id.setter
    def payment_order_id(self, payment_order_id):
        """Sets the payment_order_id of this AccountTransaction.

        The unique identifier for the payment order the transaction is associated with  # noqa: E501

        :param payment_order_id: The payment_order_id of this AccountTransaction.  # noqa: E501
        :type: str
        """

        self._payment_order_id = payment_order_id

    @property
    def bulk_payment_order_id(self):
        """Gets the bulk_payment_order_id of this AccountTransaction.  # noqa: E501

        The unique identifier for the bulk payment order the transaction is associated with  # noqa: E501

        :return: The bulk_payment_order_id of this AccountTransaction.  # noqa: E501
        :rtype: str
        """
        return self._bulk_payment_order_id

    @bulk_payment_order_id.setter
    def bulk_payment_order_id(self, bulk_payment_order_id):
        """Sets the bulk_payment_order_id of this AccountTransaction.

        The unique identifier for the bulk payment order the transaction is associated with  # noqa: E501

        :param bulk_payment_order_id: The bulk_payment_order_id of this AccountTransaction.  # noqa: E501
        :type: str
        """

        self._bulk_payment_order_id = bulk_payment_order_id

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
        if issubclass(AccountTransaction, dict):
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
        if not isinstance(other, AccountTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountTransaction):
            return True

        return self.to_dict() != other.to_dict()
