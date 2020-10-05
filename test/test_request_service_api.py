# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.15-master.10
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import madana_apiclient
from madana_apiclient.api.request_service_api import RequestServiceApi  # noqa: E501
from madana_apiclient.rest import ApiException


class TestRequestServiceApi(unittest.TestCase):
    """RequestServiceApi unit test stubs"""

    def setUp(self):
        self.api = madana_apiclient.api.request_service_api.RequestServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_data(self):
        """Test case for add_data

        Is used to upload and park the data till the AnalysisRequest gets processed.  # noqa: E501
        """
        pass

    def test_cancel_processing(self):
        """Test case for cancel_processing

        Endpoint is called from the Analysis Processing entity to submit the result.  # noqa: E501
        """
        pass

    def test_create_new_request(self):
        """Test case for create_new_request

        Endpoint used to create a new Analysis Request.  # noqa: E501
        """
        pass

    def test_get_actions(self):
        """Test case for get_actions

        """
        pass

    def test_get_agent(self):
        """Test case for get_agent

        Is called from the APE to request all parked datasets.  # noqa: E501
        """
        pass

    def test_get_all_requests(self):
        """Test case for get_all_requests

        Returns UUIDs of existing analyses.  # noqa: E501
        """
        pass

    def test_get_data(self):
        """Test case for get_data

        Is called from the APE to request all parked datasets.  # noqa: E501
        """
        pass

    def test_get_request(self):
        """Test case for get_request

        Returns the details for certain Request.  # noqa: E501
        """
        pass

    def test_get_result(self):
        """Test case for get_result

        Can be called from creator to request the AnalysisResult.  # noqa: E501
        """
        pass

    def test_get_status(self):
        """Test case for get_status

        """
        pass

    def test_give_consent(self):
        """Test case for give_consent

        Used to give consent for request.  # noqa: E501
        """
        pass

    def test_init_request_parameters(self):
        """Test case for init_request_parameters

        Endpoint used initialized addition datacollection parameters for requester.  # noqa: E501
        """
        pass

    def test_set_agent(self):
        """Test case for set_agent

        Is called from the APE to request all parked datasets.  # noqa: E501
        """
        pass

    def test_set_result(self):
        """Test case for set_result

        Endpoint is called from the Analysis Processing entity to submit the result.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
