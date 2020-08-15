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


class XmlNs0MDNUserProfileImageAllOf(object):
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
        'id': 'str',
        'image': 'str'
    }

    attribute_map = {
        'id': 'id',
        'image': 'image'
    }

    def __init__(self, id=None, image=None, local_vars_configuration=None):  # noqa: E501
        """XmlNs0MDNUserProfileImageAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._image = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if image is not None:
            self.image = image

    @property
    def id(self):
        """Gets the id of this XmlNs0MDNUserProfileImageAllOf.  # noqa: E501

          # noqa: E501

        :return: The id of this XmlNs0MDNUserProfileImageAllOf.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this XmlNs0MDNUserProfileImageAllOf.

          # noqa: E501

        :param id: The id of this XmlNs0MDNUserProfileImageAllOf.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this XmlNs0MDNUserProfileImageAllOf.  # noqa: E501

          # noqa: E501

        :return: The image of this XmlNs0MDNUserProfileImageAllOf.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this XmlNs0MDNUserProfileImageAllOf.

          # noqa: E501

        :param image: The image of this XmlNs0MDNUserProfileImageAllOf.  # noqa: E501
        :type: str
        """

        self._image = image

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
        if not isinstance(other, XmlNs0MDNUserProfileImageAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XmlNs0MDNUserProfileImageAllOf):
            return True

        return self.to_dict() != other.to_dict()
