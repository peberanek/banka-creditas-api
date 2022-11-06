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


class ErrorTransactionAuthorizationData(object):
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
        'authorization_key': 'str',
        'authorization_method': 'list[str]'
    }

    attribute_map = {
        'authorization_key': 'authorizationKey',
        'authorization_method': 'authorizationMethod'
    }

    def __init__(self, authorization_key=None, authorization_method=None, _configuration=None):  # noqa: E501
        """ErrorTransactionAuthorizationData - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._authorization_key = None
        self._authorization_method = None
        self.discriminator = None

        if authorization_key is not None:
            self.authorization_key = authorization_key
        if authorization_method is not None:
            self.authorization_method = authorization_method

    @property
    def authorization_key(self):
        """Gets the authorization_key of this ErrorTransactionAuthorizationData.  # noqa: E501

        The unique identifier for authorization transaction  # noqa: E501

        :return: The authorization_key of this ErrorTransactionAuthorizationData.  # noqa: E501
        :rtype: str
        """
        return self._authorization_key

    @authorization_key.setter
    def authorization_key(self, authorization_key):
        """Sets the authorization_key of this ErrorTransactionAuthorizationData.

        The unique identifier for authorization transaction  # noqa: E501

        :param authorization_key: The authorization_key of this ErrorTransactionAuthorizationData.  # noqa: E501
        :type: str
        """

        self._authorization_key = authorization_key

    @property
    def authorization_method(self):
        """Gets the authorization_method of this ErrorTransactionAuthorizationData.  # noqa: E501

        The list of available authorization methods (MPIN, SMS, IB)  # noqa: E501

        :return: The authorization_method of this ErrorTransactionAuthorizationData.  # noqa: E501
        :rtype: list[str]
        """
        return self._authorization_method

    @authorization_method.setter
    def authorization_method(self, authorization_method):
        """Sets the authorization_method of this ErrorTransactionAuthorizationData.

        The list of available authorization methods (MPIN, SMS, IB)  # noqa: E501

        :param authorization_method: The authorization_method of this ErrorTransactionAuthorizationData.  # noqa: E501
        :type: list[str]
        """

        self._authorization_method = authorization_method

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
        if issubclass(ErrorTransactionAuthorizationData, dict):
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
        if not isinstance(other, ErrorTransactionAuthorizationData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorTransactionAuthorizationData):
            return True

        return self.to_dict() != other.to_dict()
