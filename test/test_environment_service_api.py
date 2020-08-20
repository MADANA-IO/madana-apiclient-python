# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.14-master.20
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import madana_apiclient
from madana_apiclient.api.environment_service_api import EnvironmentServiceApi  # noqa: E501
from madana_apiclient.rest import ApiException


class TestEnvironmentServiceApi(unittest.TestCase):
    """EnvironmentServiceApi unit test stubs"""

    def setUp(self):
        self.api = madana_apiclient.api.environment_service_api.EnvironmentServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_environment(self):
        """Test case for delete_environment

        """
        pass

    def test_delete_environment_subscription(self):
        """Test case for delete_environment_subscription

        """
        pass

    def test_get_environment(self):
        """Test case for get_environment

        """
        pass

    def test_get_environments(self):
        """Test case for get_environments

        Returns UUIDs of existing analyses.  # noqa: E501
        """
        pass

    def test_get_published_environments(self):
        """Test case for get_published_environments

        """
        pass

    def test_get_subscribed_environments(self):
        """Test case for get_subscribed_environments

        """
        pass

    def test_publish_environment(self):
        """Test case for publish_environment

        """
        pass

    def test_subscribe_environment(self):
        """Test case for subscribe_environment

        """
        pass

    def test_update_environment(self):
        """Test case for update_environment

        """
        pass


if __name__ == '__main__':
    unittest.main()
