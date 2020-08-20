# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.14-master.21
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from madana_apiclient.configuration import Configuration


class JsonNodeInfo(object):
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
        'hardware_firmware': 'str',
        'cpu_model': 'str',
        'public_key': 'str',
        'cpu_logical_count': 'int',
        'owner': 'str',
        'cpu_frequency': 'str',
        'memory': 'str',
        'status': 'str',
        'hardware_baseboard': 'str',
        'cpu_family': 'str',
        'connection_url': 'str',
        'cpu_physical_cores': 'int',
        'ipfs_info': 'JsonIPFSSystemInfo',
        'processors': 'list[str]',
        'operating_system_uptime': 'float',
        'operating_system': 'str'
    }

    attribute_map = {
        'hardware_firmware': 'hardwareFirmware',
        'cpu_model': 'cpuModel',
        'public_key': 'publicKey',
        'cpu_logical_count': 'cpuLogicalCount',
        'owner': 'owner',
        'cpu_frequency': 'cpuFrequency',
        'memory': 'memory',
        'status': 'status',
        'hardware_baseboard': 'hardwareBaseboard',
        'cpu_family': 'cpuFamily',
        'connection_url': 'connectionURL',
        'cpu_physical_cores': 'cpuPhysicalCores',
        'ipfs_info': 'ipfsInfo',
        'processors': 'processors',
        'operating_system_uptime': 'operatingSystemUptime',
        'operating_system': 'operatingSystem'
    }

    def __init__(self, hardware_firmware=None, cpu_model=None, public_key=None, cpu_logical_count=None, owner=None, cpu_frequency=None, memory=None, status=None, hardware_baseboard=None, cpu_family=None, connection_url=None, cpu_physical_cores=None, ipfs_info=None, processors=None, operating_system_uptime=None, operating_system=None, local_vars_configuration=None):  # noqa: E501
        """JsonNodeInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hardware_firmware = None
        self._cpu_model = None
        self._public_key = None
        self._cpu_logical_count = None
        self._owner = None
        self._cpu_frequency = None
        self._memory = None
        self._status = None
        self._hardware_baseboard = None
        self._cpu_family = None
        self._connection_url = None
        self._cpu_physical_cores = None
        self._ipfs_info = None
        self._processors = None
        self._operating_system_uptime = None
        self._operating_system = None
        self.discriminator = None

        if hardware_firmware is not None:
            self.hardware_firmware = hardware_firmware
        if cpu_model is not None:
            self.cpu_model = cpu_model
        if public_key is not None:
            self.public_key = public_key
        if cpu_logical_count is not None:
            self.cpu_logical_count = cpu_logical_count
        if owner is not None:
            self.owner = owner
        if cpu_frequency is not None:
            self.cpu_frequency = cpu_frequency
        if memory is not None:
            self.memory = memory
        if status is not None:
            self.status = status
        if hardware_baseboard is not None:
            self.hardware_baseboard = hardware_baseboard
        if cpu_family is not None:
            self.cpu_family = cpu_family
        if connection_url is not None:
            self.connection_url = connection_url
        if cpu_physical_cores is not None:
            self.cpu_physical_cores = cpu_physical_cores
        if ipfs_info is not None:
            self.ipfs_info = ipfs_info
        if processors is not None:
            self.processors = processors
        if operating_system_uptime is not None:
            self.operating_system_uptime = operating_system_uptime
        if operating_system is not None:
            self.operating_system = operating_system

    @property
    def hardware_firmware(self):
        """Gets the hardware_firmware of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The hardware_firmware of this JsonNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._hardware_firmware

    @hardware_firmware.setter
    def hardware_firmware(self, hardware_firmware):
        """Sets the hardware_firmware of this JsonNodeInfo.

          # noqa: E501

        :param hardware_firmware: The hardware_firmware of this JsonNodeInfo.  # noqa: E501
        :type: str
        """

        self._hardware_firmware = hardware_firmware

    @property
    def cpu_model(self):
        """Gets the cpu_model of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The cpu_model of this JsonNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._cpu_model

    @cpu_model.setter
    def cpu_model(self, cpu_model):
        """Sets the cpu_model of this JsonNodeInfo.

          # noqa: E501

        :param cpu_model: The cpu_model of this JsonNodeInfo.  # noqa: E501
        :type: str
        """

        self._cpu_model = cpu_model

    @property
    def public_key(self):
        """Gets the public_key of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The public_key of this JsonNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this JsonNodeInfo.

          # noqa: E501

        :param public_key: The public_key of this JsonNodeInfo.  # noqa: E501
        :type: str
        """

        self._public_key = public_key

    @property
    def cpu_logical_count(self):
        """Gets the cpu_logical_count of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The cpu_logical_count of this JsonNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._cpu_logical_count

    @cpu_logical_count.setter
    def cpu_logical_count(self, cpu_logical_count):
        """Sets the cpu_logical_count of this JsonNodeInfo.

          # noqa: E501

        :param cpu_logical_count: The cpu_logical_count of this JsonNodeInfo.  # noqa: E501
        :type: int
        """

        self._cpu_logical_count = cpu_logical_count

    @property
    def owner(self):
        """Gets the owner of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The owner of this JsonNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this JsonNodeInfo.

          # noqa: E501

        :param owner: The owner of this JsonNodeInfo.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def cpu_frequency(self):
        """Gets the cpu_frequency of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The cpu_frequency of this JsonNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._cpu_frequency

    @cpu_frequency.setter
    def cpu_frequency(self, cpu_frequency):
        """Sets the cpu_frequency of this JsonNodeInfo.

          # noqa: E501

        :param cpu_frequency: The cpu_frequency of this JsonNodeInfo.  # noqa: E501
        :type: str
        """

        self._cpu_frequency = cpu_frequency

    @property
    def memory(self):
        """Gets the memory of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The memory of this JsonNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this JsonNodeInfo.

          # noqa: E501

        :param memory: The memory of this JsonNodeInfo.  # noqa: E501
        :type: str
        """

        self._memory = memory

    @property
    def status(self):
        """Gets the status of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The status of this JsonNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JsonNodeInfo.

          # noqa: E501

        :param status: The status of this JsonNodeInfo.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def hardware_baseboard(self):
        """Gets the hardware_baseboard of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The hardware_baseboard of this JsonNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._hardware_baseboard

    @hardware_baseboard.setter
    def hardware_baseboard(self, hardware_baseboard):
        """Sets the hardware_baseboard of this JsonNodeInfo.

          # noqa: E501

        :param hardware_baseboard: The hardware_baseboard of this JsonNodeInfo.  # noqa: E501
        :type: str
        """

        self._hardware_baseboard = hardware_baseboard

    @property
    def cpu_family(self):
        """Gets the cpu_family of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The cpu_family of this JsonNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._cpu_family

    @cpu_family.setter
    def cpu_family(self, cpu_family):
        """Sets the cpu_family of this JsonNodeInfo.

          # noqa: E501

        :param cpu_family: The cpu_family of this JsonNodeInfo.  # noqa: E501
        :type: str
        """

        self._cpu_family = cpu_family

    @property
    def connection_url(self):
        """Gets the connection_url of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The connection_url of this JsonNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._connection_url

    @connection_url.setter
    def connection_url(self, connection_url):
        """Sets the connection_url of this JsonNodeInfo.

          # noqa: E501

        :param connection_url: The connection_url of this JsonNodeInfo.  # noqa: E501
        :type: str
        """

        self._connection_url = connection_url

    @property
    def cpu_physical_cores(self):
        """Gets the cpu_physical_cores of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The cpu_physical_cores of this JsonNodeInfo.  # noqa: E501
        :rtype: int
        """
        return self._cpu_physical_cores

    @cpu_physical_cores.setter
    def cpu_physical_cores(self, cpu_physical_cores):
        """Sets the cpu_physical_cores of this JsonNodeInfo.

          # noqa: E501

        :param cpu_physical_cores: The cpu_physical_cores of this JsonNodeInfo.  # noqa: E501
        :type: int
        """

        self._cpu_physical_cores = cpu_physical_cores

    @property
    def ipfs_info(self):
        """Gets the ipfs_info of this JsonNodeInfo.  # noqa: E501


        :return: The ipfs_info of this JsonNodeInfo.  # noqa: E501
        :rtype: JsonIPFSSystemInfo
        """
        return self._ipfs_info

    @ipfs_info.setter
    def ipfs_info(self, ipfs_info):
        """Sets the ipfs_info of this JsonNodeInfo.


        :param ipfs_info: The ipfs_info of this JsonNodeInfo.  # noqa: E501
        :type: JsonIPFSSystemInfo
        """

        self._ipfs_info = ipfs_info

    @property
    def processors(self):
        """Gets the processors of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The processors of this JsonNodeInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._processors

    @processors.setter
    def processors(self, processors):
        """Sets the processors of this JsonNodeInfo.

          # noqa: E501

        :param processors: The processors of this JsonNodeInfo.  # noqa: E501
        :type: list[str]
        """

        self._processors = processors

    @property
    def operating_system_uptime(self):
        """Gets the operating_system_uptime of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The operating_system_uptime of this JsonNodeInfo.  # noqa: E501
        :rtype: float
        """
        return self._operating_system_uptime

    @operating_system_uptime.setter
    def operating_system_uptime(self, operating_system_uptime):
        """Sets the operating_system_uptime of this JsonNodeInfo.

          # noqa: E501

        :param operating_system_uptime: The operating_system_uptime of this JsonNodeInfo.  # noqa: E501
        :type: float
        """

        self._operating_system_uptime = operating_system_uptime

    @property
    def operating_system(self):
        """Gets the operating_system of this JsonNodeInfo.  # noqa: E501

          # noqa: E501

        :return: The operating_system of this JsonNodeInfo.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this JsonNodeInfo.

          # noqa: E501

        :param operating_system: The operating_system of this JsonNodeInfo.  # noqa: E501
        :type: str
        """

        self._operating_system = operating_system

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
        if not isinstance(other, JsonNodeInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonNodeInfo):
            return True

        return self.to_dict() != other.to_dict()
