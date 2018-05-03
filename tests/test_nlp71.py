import unittest
from nlp71 import check_word


class TestCheckWord(unittest.TestCase):
    '''Test Class of nlp71.py'''

    def test_check_word(self):
        '''test method for check_word'''

        test_value = [
            ('hoge', False),
            ('I', True),
            ('will', True)
        ]

        for v, r in test_value:
            self.assertEqual(r, check_word(v))


if __name__ == '__main__':
    unittest.main()
