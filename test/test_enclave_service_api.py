"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.5.0-master.22
    Generated by: https://openapi-generator.tech
"""


import unittest

import madana_apiclient
from madana_apiclient.api.enclave_service_api import EnclaveServiceApi  # noqa: E501


class TestEnclaveServiceApi(unittest.TestCase):
    """EnclaveServiceApi unit test stubs"""

    def setUp(self):
        self.api = EnclaveServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_history(self):
        """Test case for add_history

        """
        pass

    def test_approve_enclave(self):
        """Test case for approve_enclave

        """
        pass

    def test_assign_enclave_agent(self):
        """Test case for assign_enclave_agent

        """
        pass

    def test_attestate_enclave(self):
        """Test case for attestate_enclave

        """
        pass

    def test_create_enclave_run_request(self):
        """Test case for create_enclave_run_request

        """
        pass

    def test_get_enclave(self):
        """Test case for get_enclave

        """
        pass

    def test_get_enclave_types(self):
        """Test case for get_enclave_types

        """
        pass

    def test_get_enclaves(self):
        """Test case for get_enclaves

        Returns UUIDs of existing analyses.  # noqa: E501
        """
        pass

    def test_kill_enclave(self):
        """Test case for kill_enclave

        """
        pass


if __name__ == '__main__':
    unittest.main()
