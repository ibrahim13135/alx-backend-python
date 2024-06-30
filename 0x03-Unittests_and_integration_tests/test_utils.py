import unittest


from typing import Dict, Tuple, Union


from parameterized import parameterized


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
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict,
                                               int],
                               ) -> None:
        """
        Test that access_nested_map returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
