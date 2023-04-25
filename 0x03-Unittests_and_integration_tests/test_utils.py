#!/usr/bin/env python3
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Unittest test for AccessNestedMap"""
    Map = {"a": {"b": {"c": 10}}}
    # Good Paths
    g_path1 = "abc"
    g_path2 = ['a', 'b', 'c']
    r_g_path = g_path2[:]
    r_g_path.pop()

    def setUp(self):
        """
        Testing Class variables
        """
        self.assertIsInstance(self.Map, dict)
        self.assertIsInstance(self.g_path1, str)
        self.assertIsInstance(self.g_path2, list)
        self.assertIsInstance(self.r_g_path, list)

    def test_invalid_path(self):
        """
        Test case where the path not valid should raise a TypeError,
        or KeyError
        """
        with self.assertRaises(TypeError):
            access_nested_map(self.Map, None)
        with self.assertRaises(TypeError):
            access_nested_map(self.Map, 9)
        with self.assertRaises(KeyError):
            '''String is interable, so the error will be a keyError
            not a TypeError'''
            access_nested_map(self.Map, "p")
        with self.assertRaises(KeyError):
            mock = self.g_path2[:]
            mock.pop()
            mock.append('d')
            access_nested_map(self.Map, mock)

    def test_valid_path(self):
        """
        Test case where the path valid should return Any
        """
        self.assertEqual(access_nested_map(self.Map, self.g_path1), 10)
        self.assertEqual(access_nested_map(self.Map, self.g_path2), 10)
        self.assertIsInstance(access_nested_map(self.Map, self.g_path1), int)

    def test_empty_nested_dictionary(self):
        """
        Test case where the nested dictionary has a value of an empty
        dictionary: access_nested_map({"a": {"b": {}}}, ["a", "b"])
        should return {}
        """
        mock = {"a": {"b": {}}}
        self.assertEqual(access_nested_map(mock, self.r_g_path), {})

    def test_empty_list_nested_dictionary(self):
        """
        Test case where the nested dictionary has a value of an empty
        list: access_nested_map({"a": {"b": []}}, ["a", "b"]) should
        return [].
        """
        mock = {"a": {"b": []}}
        self.assertEqual(access_nested_map(mock, self.r_g_path), [])

    def test_false_value_nested_dictionary(self):
        """
        Test case where the nested dictionary has a value of False:
        access_nested_map({"a": {"b": False}}, ["a", "b"]) should
        return False.
        """
        mock = {"a": {"b": False}}
        self.assertIs(access_nested_map(mock, self.r_g_path), False)

    def test_None_value_nested_dictionary(self):
        """
        Test case where the nested dictionary has a value of None:
        access_nested_map({"a": {"b": None}}, ["a", "b"]) should
        return None.
        """
        mock = {"a": {"b": None}}
        self.assertIs(access_nested_map(mock, self.r_g_path), None)

    def test_dict_value_nested_dictionary(self):
        """
        Test case where the path contains a nested dictionary:
        access_nested_map({"a": {"b": {"c": 0}}}, ["a", "b"]) should
        return {"c": 1}.
        """
        mock = {"a": {"b": {"c": 0}}}
        self.assertEqual(access_nested_map(mock, self.r_g_path), {"c": 0})
