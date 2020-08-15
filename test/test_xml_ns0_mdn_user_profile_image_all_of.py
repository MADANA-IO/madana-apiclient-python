# coding: utf-8

"""
    madana-api

    <h1>API Quickstart Guide</h1>        <p>This documentation contains a Quickstart Guide, a few <a href=\"downloads.html\">sample clients</a>  for download and information about the available  <a href=\"resources.html\">endpoints</a>  and  <a href=\"data.html\">DataTypes</a>  </p>     <p>The <a target=\"_blank\" href=\"http://madana-explorer-staging.eu-central-1.elasticbeanstalk.com/login\">  MADANA Explorer</a> can be used to verify the interactions with the API</p>           <p>Internal use only. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a></p>         <br> <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import madana_sampleclient_python
from madana_sampleclient_python.models.xml_ns0_mdn_user_profile_image_all_of import XmlNs0MDNUserProfileImageAllOf  # noqa: E501
from madana_sampleclient_python.rest import ApiException

class TestXmlNs0MDNUserProfileImageAllOf(unittest.TestCase):
    """XmlNs0MDNUserProfileImageAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XmlNs0MDNUserProfileImageAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = madana_sampleclient_python.models.xml_ns0_mdn_user_profile_image_all_of.XmlNs0MDNUserProfileImageAllOf()  # noqa: E501
        if include_optional :
            return XmlNs0MDNUserProfileImageAllOf(
                id = '0', 
                image = '0'
            )
        else :
            return XmlNs0MDNUserProfileImageAllOf(
        )

    def testXmlNs0MDNUserProfileImageAllOf(self):
        """Test XmlNs0MDNUserProfileImageAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
