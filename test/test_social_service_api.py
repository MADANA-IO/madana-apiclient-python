"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.5.0-master.51
    Generated by: https://openapi-generator.tech
"""


import unittest

import madana_apiclient
from madana_apiclient.api.social_service_api import SocialServiceApi  # noqa: E501


class TestSocialServiceApi(unittest.TestCase):
    """SocialServiceApi unit test stubs"""

    def setUp(self):
        self.api = SocialServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_my_profile(self):
        """Test case for get_my_profile

        """
        pass

    def test_get_platforms2(self):
        """Test case for get_platforms2

        Returns all Platforms / Systems that can be Connected to the MADANA Service.  # noqa: E501
        """
        pass

    def test_get_ranking(self):
        """Test case for get_ranking

        Returns the Ranking by PTS within the System.  # noqa: E501
        """
        pass

    def test_get_social_platform_feed(self):
        """Test case for get_social_platform_feed

        """
        pass

    def test_get_user_profile(self):
        """Test case for get_user_profile

        """
        pass

    def test_get_user_profile_0(self):
        """Test case for get_user_profile_0

        """
        pass


if __name__ == '__main__':
    unittest.main()
