# coding: utf-8

"""
    madana-api

    <h1>API Quickstart Guide</h1>        <p>This documentation contains a Quickstart Guide, a few <a href=\"downloads.html\">sample clients</a>  for download and information about the available  <a href=\"resources.html\">endpoints</a>  and  <a href=\"data.html\">DataTypes</a>  </p>     <p>The <a target=\"_blank\" href=\"http://madana-explorer-staging.eu-central-1.elasticbeanstalk.com/login\">  MADANA Explorer</a> can be used to verify the interactions with the API</p>           <p>Internal use only. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a></p>         <br> <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from madana_sampleclient_python.configuration import Configuration


class JsonAnalysisRequest(object):
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
        'token_amount': 'str',
        'treshold': 'str',
        'data_collection_method': 'str',
        'data_collection_config': 'str',
        'description': 'str'
    }

    attribute_map = {
        'token_amount': 'tokenAmount',
        'treshold': 'treshold',
        'data_collection_method': 'dataCollectionMethod',
        'data_collection_config': 'dataCollectionConfig',
        'description': 'description'
    }

    def __init__(self, token_amount=None, treshold=None, data_collection_method=None, data_collection_config=None, description=None, local_vars_configuration=None):  # noqa: E501
        """JsonAnalysisRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._token_amount = None
        self._treshold = None
        self._data_collection_method = None
        self._data_collection_config = None
        self._description = None
        self.discriminator = None

        if token_amount is not None:
            self.token_amount = token_amount
        if treshold is not None:
            self.treshold = treshold
        if data_collection_method is not None:
            self.data_collection_method = data_collection_method
        if data_collection_config is not None:
            self.data_collection_config = data_collection_config
        if description is not None:
            self.description = description

    @property
    def token_amount(self):
        """Gets the token_amount of this JsonAnalysisRequest.  # noqa: E501

          # noqa: E501

        :return: The token_amount of this JsonAnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._token_amount

    @token_amount.setter
    def token_amount(self, token_amount):
        """Sets the token_amount of this JsonAnalysisRequest.

          # noqa: E501

        :param token_amount: The token_amount of this JsonAnalysisRequest.  # noqa: E501
        :type: str
        """

        self._token_amount = token_amount

    @property
    def treshold(self):
        """Gets the treshold of this JsonAnalysisRequest.  # noqa: E501

          # noqa: E501

        :return: The treshold of this JsonAnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._treshold

    @treshold.setter
    def treshold(self, treshold):
        """Sets the treshold of this JsonAnalysisRequest.

          # noqa: E501

        :param treshold: The treshold of this JsonAnalysisRequest.  # noqa: E501
        :type: str
        """

        self._treshold = treshold

    @property
    def data_collection_method(self):
        """Gets the data_collection_method of this JsonAnalysisRequest.  # noqa: E501

          # noqa: E501

        :return: The data_collection_method of this JsonAnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._data_collection_method

    @data_collection_method.setter
    def data_collection_method(self, data_collection_method):
        """Sets the data_collection_method of this JsonAnalysisRequest.

          # noqa: E501

        :param data_collection_method: The data_collection_method of this JsonAnalysisRequest.  # noqa: E501
        :type: str
        """

        self._data_collection_method = data_collection_method

    @property
    def data_collection_config(self):
        """Gets the data_collection_config of this JsonAnalysisRequest.  # noqa: E501

          # noqa: E501

        :return: The data_collection_config of this JsonAnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._data_collection_config

    @data_collection_config.setter
    def data_collection_config(self, data_collection_config):
        """Sets the data_collection_config of this JsonAnalysisRequest.

          # noqa: E501

        :param data_collection_config: The data_collection_config of this JsonAnalysisRequest.  # noqa: E501
        :type: str
        """

        self._data_collection_config = data_collection_config

    @property
    def description(self):
        """Gets the description of this JsonAnalysisRequest.  # noqa: E501

          # noqa: E501

        :return: The description of this JsonAnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JsonAnalysisRequest.

          # noqa: E501

        :param description: The description of this JsonAnalysisRequest.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, JsonAnalysisRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonAnalysisRequest):
            return True

        return self.to_dict() != other.to_dict()