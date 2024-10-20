# coding: utf-8

"""
    BPQ API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.mail_api import MailApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMailApi(unittest.TestCase):
    """MailApi unit test stubs"""

    def setUp(self):
        self.api = MailApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_mail_bulletins_get(self):
        """Test case for mail_bulletins_get

        Get a list of all bulletins  # noqa: E501
        """
        pass

    def test_mail_get(self):
        """Test case for mail_get

        Get a list of all mail items of all types  # noqa: E501
        """
        pass

    def test_mail_id_get(self):
        """Test case for mail_id_get

        Retrieve mail item by id  # noqa: E501
        """
        pass

    def test_mail_inbox_get(self):
        """Test case for mail_inbox_get

        Inbox listing, i.e. BPQ \"My Rxed\" mail  # noqa: E501
        """
        pass

    def test_mail_personal_get(self):
        """Test case for mail_personal_get

        Get a list of all personal mail, not just mine  # noqa: E501
        """
        pass

    def test_mail_sent_get(self):
        """Test case for mail_sent_get

        Sent items, i.e. BPQ \"My Sent\" mail  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()