#!/usr/bin/env python3

import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('arek', 'demko')
        self.assertEqual(formatted_name, 'Arek Demko')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('arek', 'demko', 'marcin')
        self.assertEqual(formatted_name, 'Arek Marcin Demko')

if __name__ == '__main__':
    unittest.main()
