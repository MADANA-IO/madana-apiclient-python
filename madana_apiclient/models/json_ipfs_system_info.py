# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.14-master.17
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from madana_apiclient.configuration import Configuration


class JsonIPFSSystemInfo(object):
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
        'swarm_connection': 'str',
        'public_key': 'str',
        'protocol_version': 'str',
        'agent_version': 'str',
        'id': 'str'
    }

    attribute_map = {
        'swarm_connection': 'swarmConnection',
        'public_key': 'publicKey',
        'protocol_version': 'protocolVersion',
        'agent_version': 'agentVersion',
        'id': 'id'
    }

    def __init__(self, swarm_connection=None, public_key=None, protocol_version=None, agent_version=None, id=None, local_vars_configuration=None):  # noqa: E501
        """JsonIPFSSystemInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._swarm_connection = None
        self._public_key = None
        self._protocol_version = None
        self._agent_version = None
        self._id = None
        self.discriminator = None

        if swarm_connection is not None:
            self.swarm_connection = swarm_connection
        if public_key is not None:
            self.public_key = public_key
        if protocol_version is not None:
            self.protocol_version = protocol_version
        if agent_version is not None:
            self.agent_version = agent_version
        if id is not None:
            self.id = id

    @property
    def swarm_connection(self):
        """Gets the swarm_connection of this JsonIPFSSystemInfo.  # noqa: E501

          # noqa: E501

        :return: The swarm_connection of this JsonIPFSSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._swarm_connection

    @swarm_connection.setter
    def swarm_connection(self, swarm_connection):
        """Sets the swarm_connection of this JsonIPFSSystemInfo.

          # noqa: E501

        :param swarm_connection: The swarm_connection of this JsonIPFSSystemInfo.  # noqa: E501
        :type: str
        """

        self._swarm_connection = swarm_connection

    @property
    def public_key(self):
        """Gets the public_key of this JsonIPFSSystemInfo.  # noqa: E501

          # noqa: E501

        :return: The public_key of this JsonIPFSSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this JsonIPFSSystemInfo.

          # noqa: E501

        :param public_key: The public_key of this JsonIPFSSystemInfo.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

    @property
    def protocol_version(self):
        """Gets the protocol_version of this JsonIPFSSystemInfo.  # noqa: E501

          # noqa: E501

        :return: The protocol_version of this JsonIPFSSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this JsonIPFSSystemInfo.

          # noqa: E501

        :param protocol_version: The protocol_version of this JsonIPFSSystemInfo.  # noqa: E501
        :type: str
        """

        self._protocol_version = protocol_version

    @property
    def agent_version(self):
        """Gets the agent_version of this JsonIPFSSystemInfo.  # noqa: E501

          # noqa: E501

        :return: The agent_version of this JsonIPFSSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this JsonIPFSSystemInfo.

          # noqa: E501

        :param agent_version: The agent_version of this JsonIPFSSystemInfo.  # noqa: E501
        :type: str
        """

        self._agent_version = agent_version

    @property
    def id(self):
        """Gets the id of this JsonIPFSSystemInfo.  # noqa: E501

          # noqa: E501

        :return: The id of this JsonIPFSSystemInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JsonIPFSSystemInfo.

          # noqa: E501

        :param id: The id of this JsonIPFSSystemInfo.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, JsonIPFSSystemInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonIPFSSystemInfo):
            return True

        return self.to_dict() != other.to_dict()