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


class JsonEnvironmentPublishingRequest(object):
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
        'description': 'str',
        'ipfs_hash': 'str',
        'size': 'str',
        'is_public': 'str',
        'name': 'str',
        'uuid': 'str',
        'content': 'str',
        'ipfs_primary_peer': 'str',
        'packages': 'str'
    }

    attribute_map = {
        'description': 'description',
        'ipfs_hash': 'ipfsHash',
        'size': 'size',
        'is_public': 'isPublic',
        'name': 'name',
        'uuid': 'uuid',
        'content': 'content',
        'ipfs_primary_peer': 'ipfsPrimaryPeer',
        'packages': 'packages'
    }

    def __init__(self, description=None, ipfs_hash=None, size=None, is_public=None, name=None, uuid=None, content=None, ipfs_primary_peer=None, packages=None, local_vars_configuration=None):  # noqa: E501
        """JsonEnvironmentPublishingRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._ipfs_hash = None
        self._size = None
        self._is_public = None
        self._name = None
        self._uuid = None
        self._content = None
        self._ipfs_primary_peer = None
        self._packages = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if ipfs_hash is not None:
            self.ipfs_hash = ipfs_hash
        if size is not None:
            self.size = size
        if is_public is not None:
            self.is_public = is_public
        if name is not None:
            self.name = name
        if uuid is not None:
            self.uuid = uuid
        if content is not None:
            self.content = content
        if ipfs_primary_peer is not None:
            self.ipfs_primary_peer = ipfs_primary_peer
        if packages is not None:
            self.packages = packages

    @property
    def description(self):
        """Gets the description of this JsonEnvironmentPublishingRequest.  # noqa: E501

          # noqa: E501

        :return: The description of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JsonEnvironmentPublishingRequest.

          # noqa: E501

        :param description: The description of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ipfs_hash(self):
        """Gets the ipfs_hash of this JsonEnvironmentPublishingRequest.  # noqa: E501

          # noqa: E501

        :return: The ipfs_hash of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :rtype: str
        """
        return self._ipfs_hash

    @ipfs_hash.setter
    def ipfs_hash(self, ipfs_hash):
        """Sets the ipfs_hash of this JsonEnvironmentPublishingRequest.

          # noqa: E501

        :param ipfs_hash: The ipfs_hash of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :type: str
        """

        self._ipfs_hash = ipfs_hash

    @property
    def size(self):
        """Gets the size of this JsonEnvironmentPublishingRequest.  # noqa: E501

          # noqa: E501

        :return: The size of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this JsonEnvironmentPublishingRequest.

          # noqa: E501

        :param size: The size of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def is_public(self):
        """Gets the is_public of this JsonEnvironmentPublishingRequest.  # noqa: E501

          # noqa: E501

        :return: The is_public of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :rtype: str
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this JsonEnvironmentPublishingRequest.

          # noqa: E501

        :param is_public: The is_public of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :type: str
        """

        self._is_public = is_public

    @property
    def name(self):
        """Gets the name of this JsonEnvironmentPublishingRequest.  # noqa: E501

          # noqa: E501

        :return: The name of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JsonEnvironmentPublishingRequest.

          # noqa: E501

        :param name: The name of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this JsonEnvironmentPublishingRequest.  # noqa: E501

          # noqa: E501

        :return: The uuid of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this JsonEnvironmentPublishingRequest.

          # noqa: E501

        :param uuid: The uuid of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def content(self):
        """Gets the content of this JsonEnvironmentPublishingRequest.  # noqa: E501

          # noqa: E501

        :return: The content of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this JsonEnvironmentPublishingRequest.

          # noqa: E501

        :param content: The content of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def ipfs_primary_peer(self):
        """Gets the ipfs_primary_peer of this JsonEnvironmentPublishingRequest.  # noqa: E501

          # noqa: E501

        :return: The ipfs_primary_peer of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :rtype: str
        """
        return self._ipfs_primary_peer

    @ipfs_primary_peer.setter
    def ipfs_primary_peer(self, ipfs_primary_peer):
        """Sets the ipfs_primary_peer of this JsonEnvironmentPublishingRequest.

          # noqa: E501

        :param ipfs_primary_peer: The ipfs_primary_peer of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :type: str
        """

        self._ipfs_primary_peer = ipfs_primary_peer

    @property
    def packages(self):
        """Gets the packages of this JsonEnvironmentPublishingRequest.  # noqa: E501

          # noqa: E501

        :return: The packages of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :rtype: str
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this JsonEnvironmentPublishingRequest.

          # noqa: E501

        :param packages: The packages of this JsonEnvironmentPublishingRequest.  # noqa: E501
        :type: str
        """

        self._packages = packages

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
        if not isinstance(other, JsonEnvironmentPublishingRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonEnvironmentPublishingRequest):
            return True

        return self.to_dict() != other.to_dict()
