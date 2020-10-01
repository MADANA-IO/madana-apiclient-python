# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.15-master.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from madana_apiclient.configuration import Configuration


class JsonMDNUserAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'social_accounts': 'list[JsonMDNSocialUserObject]',
        'guid': 'str',
        'last_name': 'str',
        'settings': 'list[JsonMDNUserSetting]',
        'first_name': 'str',
        'credentials': 'JsonMDNUserCredentials',
        'mail': 'str'
    }

    attribute_map = {
        'social_accounts': 'socialAccounts',
        'guid': 'guid',
        'last_name': 'lastName',
        'settings': 'settings',
        'first_name': 'firstName',
        'credentials': 'credentials',
        'mail': 'mail'
    }

    def __init__(self, social_accounts=None, guid=None, last_name=None, settings=None, first_name=None, credentials=None, mail=None, local_vars_configuration=None):  # noqa: E501
        """JsonMDNUserAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._social_accounts = None
        self._guid = None
        self._last_name = None
        self._settings = None
        self._first_name = None
        self._credentials = None
        self._mail = None
        self.discriminator = None

        if social_accounts is not None:
            self.social_accounts = social_accounts
        if guid is not None:
            self.guid = guid
        if last_name is not None:
            self.last_name = last_name
        if settings is not None:
            self.settings = settings
        if first_name is not None:
            self.first_name = first_name
        if credentials is not None:
            self.credentials = credentials
        if mail is not None:
            self.mail = mail

    @property
    def social_accounts(self):
        """Gets the social_accounts of this JsonMDNUserAllOf.  # noqa: E501

          # noqa: E501

        :return: The social_accounts of this JsonMDNUserAllOf.  # noqa: E501
        :rtype: list[JsonMDNSocialUserObject]
        """
        return self._social_accounts

    @social_accounts.setter
    def social_accounts(self, social_accounts):
        """Sets the social_accounts of this JsonMDNUserAllOf.

          # noqa: E501

        :param social_accounts: The social_accounts of this JsonMDNUserAllOf.  # noqa: E501
        :type social_accounts: list[JsonMDNSocialUserObject]
        """

        self._social_accounts = social_accounts

    @property
    def guid(self):
        """Gets the guid of this JsonMDNUserAllOf.  # noqa: E501

          # noqa: E501

        :return: The guid of this JsonMDNUserAllOf.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this JsonMDNUserAllOf.

          # noqa: E501

        :param guid: The guid of this JsonMDNUserAllOf.  # noqa: E501
        :type guid: str
        """

        self._guid = guid

    @property
    def last_name(self):
        """Gets the last_name of this JsonMDNUserAllOf.  # noqa: E501

          # noqa: E501

        :return: The last_name of this JsonMDNUserAllOf.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this JsonMDNUserAllOf.

          # noqa: E501

        :param last_name: The last_name of this JsonMDNUserAllOf.  # noqa: E501
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def settings(self):
        """Gets the settings of this JsonMDNUserAllOf.  # noqa: E501

          # noqa: E501

        :return: The settings of this JsonMDNUserAllOf.  # noqa: E501
        :rtype: list[JsonMDNUserSetting]
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this JsonMDNUserAllOf.

          # noqa: E501

        :param settings: The settings of this JsonMDNUserAllOf.  # noqa: E501
        :type settings: list[JsonMDNUserSetting]
        """

        self._settings = settings

    @property
    def first_name(self):
        """Gets the first_name of this JsonMDNUserAllOf.  # noqa: E501

          # noqa: E501

        :return: The first_name of this JsonMDNUserAllOf.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this JsonMDNUserAllOf.

          # noqa: E501

        :param first_name: The first_name of this JsonMDNUserAllOf.  # noqa: E501
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def credentials(self):
        """Gets the credentials of this JsonMDNUserAllOf.  # noqa: E501


        :return: The credentials of this JsonMDNUserAllOf.  # noqa: E501
        :rtype: JsonMDNUserCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this JsonMDNUserAllOf.


        :param credentials: The credentials of this JsonMDNUserAllOf.  # noqa: E501
        :type credentials: JsonMDNUserCredentials
        """

        self._credentials = credentials

    @property
    def mail(self):
        """Gets the mail of this JsonMDNUserAllOf.  # noqa: E501

          # noqa: E501

        :return: The mail of this JsonMDNUserAllOf.  # noqa: E501
        :rtype: str
        """
        return self._mail

    @mail.setter
    def mail(self, mail):
        """Sets the mail of this JsonMDNUserAllOf.

          # noqa: E501

        :param mail: The mail of this JsonMDNUserAllOf.  # noqa: E501
        :type mail: str
        """

        self._mail = mail

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JsonMDNUserAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonMDNUserAllOf):
            return True

        return self.to_dict() != other.to_dict()
