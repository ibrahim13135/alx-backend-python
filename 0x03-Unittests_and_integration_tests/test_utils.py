#!/usr/bin/env python3

from client import GithubOrgClient
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from unittest.mock import patch, Mock

from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient

class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class to test access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int],
                               ) -> None:
        """
        Test that access_nested_map returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        exception: Exception,
    ) -> None:
        """
        Test that access_nested_map raises the expected exception.
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), str(path[-1]))

# task 2


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class to test get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected result.
        """
        with patch('utils.requests.get') as mock_get:
            # Create a mock response object
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function with the test URL
            result = get_json(test_url)

            # Assert that requests.get was called exactly once with the test
            # URL
            mock_get.assert_called_once_with(test_url)

            # Assert that the output of get_json is equal to the test_payload
            self.assertEqual(result, test_payload)

# task 4


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""

    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
        ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()


# TASK 5
# Step-by-Step Guide
# Familiarize with GithubOrgClient Class:

# The GithubOrgClient class likely has a method org which retrieves information
#  about a GitHub organization.
#  This method might internally call a get_json function to fetch data
# from a URL.
# Setup test_client.py:

# Create a new file named test_client.py.
# Import Necessary Modules:

# Import unittest, patch, parameterized, and GithubOrgClient.
# Define TestGithubOrgClient Class:

# This class will inherit from unittest.TestCase.
# Implement test_org Method:

# Use @patch to mock get_json so no actual HTTP requests are made.
# Use @parameterized.expand to test multiple organization names.
# Test that GithubOrgClient.org returns the correct value and that
# get_json is called with the expected arguments.


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ('google',),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        mock_get_json.return_value = {"login": org_name}
        client = GithubOrgClient(org_name)

        res1 = client.org()
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(res1, {"login": org_name})
