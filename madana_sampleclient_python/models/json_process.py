# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.14-master.16
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from madana_sampleclient_python.configuration import Configuration


class JsonProcess(object):
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
        'input_stream': 'object',
        'alive': 'bool',
        'error_stream': 'object',
        'output_stream': 'object'
    }

    attribute_map = {
        'input_stream': 'inputStream',
        'alive': 'alive',
        'error_stream': 'errorStream',
        'output_stream': 'outputStream'
    }

    def __init__(self, input_stream=None, alive=None, error_stream=None, output_stream=None, local_vars_configuration=None):  # noqa: E501
        """JsonProcess - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._input_stream = None
        self._alive = None
        self._error_stream = None
        self._output_stream = None
        self.discriminator = None

        if input_stream is not None:
            self.input_stream = input_stream
        if alive is not None:
            self.alive = alive
        if error_stream is not None:
            self.error_stream = error_stream
        if output_stream is not None:
            self.output_stream = output_stream

    @property
    def input_stream(self):
        """Gets the input_stream of this JsonProcess.  # noqa: E501

          # noqa: E501

        :return: The input_stream of this JsonProcess.  # noqa: E501
        :rtype: object
        """
        return self._input_stream

    @input_stream.setter
    def input_stream(self, input_stream):
        """Sets the input_stream of this JsonProcess.

          # noqa: E501

        :param input_stream: The input_stream of this JsonProcess.  # noqa: E501
        :type: object
        """

        self._input_stream = input_stream

    @property
    def alive(self):
        """Gets the alive of this JsonProcess.  # noqa: E501

          # noqa: E501

        :return: The alive of this JsonProcess.  # noqa: E501
        :rtype: bool
        """
        return self._alive

    @alive.setter
    def alive(self, alive):
        """Sets the alive of this JsonProcess.

          # noqa: E501

        :param alive: The alive of this JsonProcess.  # noqa: E501
        :type: bool
        """

        self._alive = alive

    @property
    def error_stream(self):
        """Gets the error_stream of this JsonProcess.  # noqa: E501

          # noqa: E501

        :return: The error_stream of this JsonProcess.  # noqa: E501
        :rtype: object
        """
        return self._error_stream

    @error_stream.setter
    def error_stream(self, error_stream):
        """Sets the error_stream of this JsonProcess.

          # noqa: E501

        :param error_stream: The error_stream of this JsonProcess.  # noqa: E501
        :type: object
        """

        self._error_stream = error_stream

    @property
    def output_stream(self):
        """Gets the output_stream of this JsonProcess.  # noqa: E501

          # noqa: E501

        :return: The output_stream of this JsonProcess.  # noqa: E501
        :rtype: object
        """
        return self._output_stream

    @output_stream.setter
    def output_stream(self, output_stream):
        """Sets the output_stream of this JsonProcess.

          # noqa: E501

        :param output_stream: The output_stream of this JsonProcess.  # noqa: E501
        :type: object
        """

        self._output_stream = output_stream

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
        if not isinstance(other, JsonProcess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonProcess):
            return True

        return self.to_dict() != other.to_dict()
