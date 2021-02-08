"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.5.0-master.50
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
    from madana_apiclient.model.json_v1_managed_fields_entry import JsonV1ManagedFieldsEntry
    from madana_apiclient.model.json_v1_owner_reference import JsonV1OwnerReference
    globals()['JsonV1ManagedFieldsEntry'] = JsonV1ManagedFieldsEntry
    globals()['JsonV1OwnerReference'] = JsonV1OwnerReference


class JsonV1ObjectMeta(ModelNormal):
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
            'managed_fields': ([JsonV1ManagedFieldsEntry],),  # noqa: E501
            'finalizers': ([str],),  # noqa: E501
            'self_link': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'cluster_name': (str,),  # noqa: E501
            'uid': (str,),  # noqa: E501
            'annotations': ({str: (str,)},),  # noqa: E501
            'resource_version': (str,),  # noqa: E501
            'generation': (float,),  # noqa: E501
            'creation_timestamp': (float,),  # noqa: E501
            'owner_references': ([JsonV1OwnerReference],),  # noqa: E501
            'deletion_grace_period_seconds': (float,),  # noqa: E501
            'namespace': (str,),  # noqa: E501
            'labels': ({str: (str,)},),  # noqa: E501
            'generate_name': (str,),  # noqa: E501
            'deletion_timestamp': (float,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'managed_fields': 'managedFields',  # noqa: E501
        'finalizers': 'finalizers',  # noqa: E501
        'self_link': 'selfLink',  # noqa: E501
        'name': 'name',  # noqa: E501
        'cluster_name': 'clusterName',  # noqa: E501
        'uid': 'uid',  # noqa: E501
        'annotations': 'annotations',  # noqa: E501
        'resource_version': 'resourceVersion',  # noqa: E501
        'generation': 'generation',  # noqa: E501
        'creation_timestamp': 'creationTimestamp',  # noqa: E501
        'owner_references': 'ownerReferences',  # noqa: E501
        'deletion_grace_period_seconds': 'deletionGracePeriodSeconds',  # noqa: E501
        'namespace': 'namespace',  # noqa: E501
        'labels': 'labels',  # noqa: E501
        'generate_name': 'generateName',  # noqa: E501
        'deletion_timestamp': 'deletionTimestamp',  # noqa: E501
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
        """JsonV1ObjectMeta - a model defined in OpenAPI

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
            managed_fields ([JsonV1ManagedFieldsEntry]): . [optional]  # noqa: E501
            finalizers ([str]): . [optional]  # noqa: E501
            self_link (str): . [optional]  # noqa: E501
            name (str): . [optional]  # noqa: E501
            cluster_name (str): . [optional]  # noqa: E501
            uid (str): . [optional]  # noqa: E501
            annotations ({str: (str,)}): . [optional]  # noqa: E501
            resource_version (str): . [optional]  # noqa: E501
            generation (float): . [optional]  # noqa: E501
            creation_timestamp (float): . [optional]  # noqa: E501
            owner_references ([JsonV1OwnerReference]): . [optional]  # noqa: E501
            deletion_grace_period_seconds (float): . [optional]  # noqa: E501
            namespace (str): . [optional]  # noqa: E501
            labels ({str: (str,)}): . [optional]  # noqa: E501
            generate_name (str): . [optional]  # noqa: E501
            deletion_timestamp (float): . [optional]  # noqa: E501
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
