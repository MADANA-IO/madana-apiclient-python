# coding: utf-8

"""
    madana-api

    <h1>API Quickstart Guide</h1>        <p>This documentation contains a Quickstart Guide, a few <a href=\"downloads.html\">sample clients</a>  for download and information about the available  <a href=\"resources.html\">endpoints</a>  and  <a href=\"data.html\">DataTypes</a>  </p>     <p>The <a target=\"_blank\" href=\"http://madana-explorer-staging.eu-central-1.elasticbeanstalk.com/login\">  MADANA Explorer</a> can be used to verify the interactions with the API</p>           <p>Internal use only. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a></p>         <br> <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.12
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import madana_sampleclient_python
from madana_sampleclient_python.api.node_service_api import NodeServiceApi  # noqa: E501
from madana_sampleclient_python.rest import ApiException


class TestNodeServiceApi(unittest.TestCase):
    """NodeServiceApi unit test stubs"""

    def setUp(self):
        self.api = madana_sampleclient_python.api.node_service_api.NodeServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_nodes2(self):
        """Test case for get_nodes2

        """
        pass

    def test_post_node_info(self):
        """Test case for post_node_info

        """
        pass


if __name__ == '__main__':
    unittest.main()
