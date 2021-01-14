"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.0.1-master.3
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from madana_apiclient.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from madana_apiclient.model.json_ipfs_system_info import JsonIPFSSystemInfo
    from madana_apiclient.model.json_sgx_info import JsonSGXInfo
    globals()['JsonIPFSSystemInfo'] = JsonIPFSSystemInfo
    globals()['JsonSGXInfo'] = JsonSGXInfo


class JsonNodeInfo(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'cpu_frequency': (str,),  # noqa: E501
            'sgx_info': (JsonSGXInfo,),  # noqa: E501
            'public_key': (str,),  # noqa: E501
            'cpu_logical_count': (int,),  # noqa: E501
            'owner': (str,),  # noqa: E501
            'cpu_physical_cores': (int,),  # noqa: E501
            'memory': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'ipfs_info': (JsonIPFSSystemInfo,),  # noqa: E501
            'hardware_firmware': (str,),  # noqa: E501
            'cpu_model': (str,),  # noqa: E501
            'operating_system': (str,),  # noqa: E501
            'processors': ([str],),  # noqa: E501
            'hardware_baseboard': (str,),  # noqa: E501
            'connection_url': (str,),  # noqa: E501
            'operating_system_uptime': (float,),  # noqa: E501
            'cpu_family': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'cpu_frequency': 'cpuFrequency',  # noqa: E501
        'sgx_info': 'sgxInfo',  # noqa: E501
        'public_key': 'publicKey',  # noqa: E501
        'cpu_logical_count': 'cpuLogicalCount',  # noqa: E501
        'owner': 'owner',  # noqa: E501
        'cpu_physical_cores': 'cpuPhysicalCores',  # noqa: E501
        'memory': 'memory',  # noqa: E501
        'status': 'status',  # noqa: E501
        'ipfs_info': 'ipfsInfo',  # noqa: E501
        'hardware_firmware': 'hardwareFirmware',  # noqa: E501
        'cpu_model': 'cpuModel',  # noqa: E501
        'operating_system': 'operatingSystem',  # noqa: E501
        'processors': 'processors',  # noqa: E501
        'hardware_baseboard': 'hardwareBaseboard',  # noqa: E501
        'connection_url': 'connectionURL',  # noqa: E501
        'operating_system_uptime': 'operatingSystemUptime',  # noqa: E501
        'cpu_family': 'cpuFamily',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """JsonNodeInfo - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            cpu_frequency (str): . [optional]  # noqa: E501
            sgx_info (JsonSGXInfo): [optional]  # noqa: E501
            public_key (str): . [optional]  # noqa: E501
            cpu_logical_count (int): . [optional]  # noqa: E501
            owner (str): . [optional]  # noqa: E501
            cpu_physical_cores (int): . [optional]  # noqa: E501
            memory (str): . [optional]  # noqa: E501
            status (str): . [optional]  # noqa: E501
            ipfs_info (JsonIPFSSystemInfo): [optional]  # noqa: E501
            hardware_firmware (str): . [optional]  # noqa: E501
            cpu_model (str): . [optional]  # noqa: E501
            operating_system (str): . [optional]  # noqa: E501
            processors ([str]): . [optional]  # noqa: E501
            hardware_baseboard (str): . [optional]  # noqa: E501
            connection_url (str): . [optional]  # noqa: E501
            operating_system_uptime (float): . [optional]  # noqa: E501
            cpu_family (str): . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
