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
from madana_sampleclient_python.api.certificate_service_api import CertificateServiceApi  # noqa: E501
from madana_sampleclient_python.rest import ApiException


class TestCertificateServiceApi(unittest.TestCase):
    """CertificateServiceApi unit test stubs"""

    def setUp(self):
        self.api = madana_sampleclient_python.api.certificate_service_api.CertificateServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authenticate_certificate(self):
        """Test case for authenticate_certificate

        Issues certificates for logged-in users.  # noqa: E501
        """
        pass

    def test_get_certificate(self):
        """Test case for get_certificate

        """
        pass

    def test_get_certificate_0(self):
        """Test case for get_certificate_0

        """
        pass


if __name__ == '__main__':
    unittest.main()
