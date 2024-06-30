import unittest


# run the test method with different sets of parameters.
from parameterized import parameterized

# Access nested map with key path.
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class to test access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

# nested_map={"a": 1}, path=("a",)
# nested_map={"a": {"b": 2}}, path=("a",)
# nested_map={"a": {"b": 2}}, path=("a", "b")

# @parameterized.expand([
#     (input1, input2, expected_output),
#     (input3, input4, expected_output),
#     ...
# ])


# @parameterized.expand([
#     ({"a": 1}, ("a",), 1),
#     ({"a": {"b": 2}}, ("a",), {"b": 2}),
#     ({"a": {"b": 2}}, ("a", "b"), 2)
# ])
