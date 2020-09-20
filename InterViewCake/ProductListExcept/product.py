#!/usr/bin/env python3
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the \
# products.

import unittest


def get_products_of_all_ints_except_at_index(int_list: list):
    return int_list


class ProductTest(unittest.TestCase):
    def three(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)