#coding: utf-8
import unittest
import doctest
import test_chinese_slugify


def suite():
    suite = unittest.TestSuite()
    suite.addTests(test_chinese_slugify.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
