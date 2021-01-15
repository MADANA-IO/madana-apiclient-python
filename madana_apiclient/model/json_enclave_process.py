"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.5.0-master.33
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
    from madana_apiclient.model.json_enclave_port import JsonEnclavePort
    from madana_apiclient.model.json_environment import JsonEnvironment
    from madana_apiclient.model.json_kubernetes_enclave import JsonKubernetesEnclave
    from madana_apiclient.model.json_process import JsonProcess
    from madana_apiclient.model.json_wireguard_interface import JsonWireguardInterface
    globals()['JsonEnclavePort'] = JsonEnclavePort
    globals()['JsonEnvironment'] = JsonEnvironment
    globals()['JsonKubernetesEnclave'] = JsonKubernetesEnclave
    globals()['JsonProcess'] = JsonProcess
    globals()['JsonWireguardInterface'] = JsonWireguardInterface


class JsonEnclaveProcess(ModelNormal):
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
            'kubernetes_enclave': (JsonKubernetesEnclave,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'enclave_inputstream': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'startup_time': (str,),  # noqa: E501
            'internal_ident': (str,),  # noqa: E501
            'wireguard_public_key': (str,),  # noqa: E501
            'attestation_server': (str,),  # noqa: E501
            'enclave_ident': (str,),  # noqa: E501
            'wg_interface': (JsonWireguardInterface,),  # noqa: E501
            'public_ident': (str,),  # noqa: E501
            'ending_time': (str,),  # noqa: E501
            'process': (JsonProcess,),  # noqa: E501
            'console_output': (str,),  # noqa: E501
            'internal_attesation_server': (str,),  # noqa: E501
            'wireguard_server': (str,),  # noqa: E501
            'port_mapping': ({str: (str,)},),  # noqa: E501
            'startup_cmd': (str,),  # noqa: E501
            'environment': (JsonEnvironment,),  # noqa: E501
            'signer_ident': (str,),  # noqa: E501
            'ports': ([JsonEnclavePort],),  # noqa: E501
            'remote_control_server': (str,),  # noqa: E501
            'internal_wireguard_server': (str,),  # noqa: E501
            'internal_remote_control_server': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'kubernetes_enclave': 'kubernetesEnclave',  # noqa: E501
        'status': 'status',  # noqa: E501
        'enclave_inputstream': 'enclaveInputstream',  # noqa: E501
        'startup_time': 'startupTime',  # noqa: E501
        'internal_ident': 'internalIdent',  # noqa: E501
        'wireguard_public_key': 'wireguardPublicKey',  # noqa: E501
        'attestation_server': 'attestationServer',  # noqa: E501
        'enclave_ident': 'enclaveIdent',  # noqa: E501
        'wg_interface': 'wgInterface',  # noqa: E501
        'public_ident': 'publicIdent',  # noqa: E501
        'ending_time': 'endingTime',  # noqa: E501
        'process': 'process',  # noqa: E501
        'console_output': 'consoleOutput',  # noqa: E501
        'internal_attesation_server': 'internalAttesationServer',  # noqa: E501
        'wireguard_server': 'wireguardServer',  # noqa: E501
        'port_mapping': 'portMapping',  # noqa: E501
        'startup_cmd': 'startupCMD',  # noqa: E501
        'environment': 'environment',  # noqa: E501
        'signer_ident': 'signerIdent',  # noqa: E501
        'ports': 'ports',  # noqa: E501
        'remote_control_server': 'remoteControlServer',  # noqa: E501
        'internal_wireguard_server': 'internalWireguardServer',  # noqa: E501
        'internal_remote_control_server': 'internalRemoteControlServer',  # noqa: E501
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
        """JsonEnclaveProcess - a model defined in OpenAPI

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
            kubernetes_enclave (JsonKubernetesEnclave): [optional]  # noqa: E501
            status (str): . [optional]  # noqa: E501
            enclave_inputstream ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): . [optional]  # noqa: E501
            startup_time (str): . [optional]  # noqa: E501
            internal_ident (str): . [optional]  # noqa: E501
            wireguard_public_key (str): . [optional]  # noqa: E501
            attestation_server (str): . [optional]  # noqa: E501
            enclave_ident (str): . [optional]  # noqa: E501
            wg_interface (JsonWireguardInterface): [optional]  # noqa: E501
            public_ident (str): . [optional]  # noqa: E501
            ending_time (str): . [optional]  # noqa: E501
            process (JsonProcess): [optional]  # noqa: E501
            console_output (str): . [optional]  # noqa: E501
            internal_attesation_server (str): . [optional]  # noqa: E501
            wireguard_server (str): . [optional]  # noqa: E501
            port_mapping ({str: (str,)}): . [optional]  # noqa: E501
            startup_cmd (str): . [optional]  # noqa: E501
            environment (JsonEnvironment): [optional]  # noqa: E501
            signer_ident (str): . [optional]  # noqa: E501
            ports ([JsonEnclavePort]): . [optional]  # noqa: E501
            remote_control_server (str): . [optional]  # noqa: E501
            internal_wireguard_server (str): . [optional]  # noqa: E501
            internal_remote_control_server (str): . [optional]  # noqa: E501
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
