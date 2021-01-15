"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.5.0-master.26
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import madana_apiclient
from madana_apiclient.model.json_mdn_social_user_object import JsonMDNSocialUserObject
from madana_apiclient.model.json_mdn_user_all_of import JsonMDNUserAllOf
from madana_apiclient.model.json_mdn_user_credentials import JsonMDNUserCredentials
from madana_apiclient.model.json_mdn_user_setting import JsonMDNUserSetting
from madana_apiclient.model.json_mdna_user_object import JsonMDNAUserObject
globals()['JsonMDNAUserObject'] = JsonMDNAUserObject
globals()['JsonMDNSocialUserObject'] = JsonMDNSocialUserObject
globals()['JsonMDNUserAllOf'] = JsonMDNUserAllOf
globals()['JsonMDNUserCredentials'] = JsonMDNUserCredentials
globals()['JsonMDNUserSetting'] = JsonMDNUserSetting
from madana_apiclient.model.json_mdn_user import JsonMDNUser


class TestJsonMDNUser(unittest.TestCase):
    """JsonMDNUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJsonMDNUser(self):
        """Test JsonMDNUser"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JsonMDNUser()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
