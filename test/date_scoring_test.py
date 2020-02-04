import unittest
from src import date_scoring


class TestDateScoring(unittest.TestCase):

    def test_date_parser_1(self):
        self.assertEqual(('2019', '12', '25'), date_scoring.parse_iso('2019-12-25'))

    def test_date_parser_2(self):
        self.assertEqual(('2019', '02', '03'), date_scoring.parse_iso('2019-02-03'))

    def test_date_parser_invalid(self):
        with self.assertRaises(ValueError):
            date_scoring.parse_iso('2019-029-03')

    def test_date_parser_empty(self):
        with self.assertRaises(ValueError):
            date_scoring.parse_iso('')

    def test_date_parser_none(self):
        with self.assertRaises(TypeError):
            date_scoring.parse_iso(None)


if __name__ == '__main__':
    unittest.main()
