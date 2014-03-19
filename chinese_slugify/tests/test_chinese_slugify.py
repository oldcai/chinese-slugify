#coding:utf-8
import unittest
from chinese_slugify import chinese_slugify


class ChineseSlugifyTestCase(unittest.TestCase):
    def test_polyphone_word(self):
        self.assertEquals(chinese_slugify(u'还是还钱吧'), 'HaiShi-Huan-Qian-Ba')

    def test_russian(self):
        self.assertEquals(chinese_slugify(u'Компьютер'), 'Kompiuter')


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromTestCase(ChineseSlugifyTestCase))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
