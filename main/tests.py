#!/usr/bin/env python3

import unittest


class TestMain(unittest.TestCase):

    def test_hello(self):
        s = "hello"
        self.assertEqual(s, "hello")


if __name__ =='__main__':
    unittest.main()
