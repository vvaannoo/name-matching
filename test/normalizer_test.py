import unittest
from src import normalizer as nrm


class TestNormalizer(unittest.TestCase):

    def test_transliterate_geo(self):
        self.assertEqual('giga kokaia.', nrm.transliterate('გიგა კოკაია.'))

    def test_transliterate_eng(self):
        self.assertEqual('Giga Kokaia.', nrm.transliterate('Giga Kokaia.'))

    def test_transliterate_mixed(self):
        self.assertEqual('Giga kokaia.', nrm.transliterate('Giga კოკაია.'))

    def test_transliterate_empty(self):
        self.assertIsNone(nrm.transliterate(''))

    def test_transliterate_none(self):
        self.assertIsNone(nrm.transliterate(None))

    def test_remove_symbols_1(self):
        self.assertEqual('g giga kokaia', nrm.remove_symbols(' g.giga -kokaia!'))

    def test_remove_symbols_without_symbols(self):
        self.assertEqual('kokaia', nrm.remove_symbols('kokaia'))

    def test_tokenize(self):
        self.assertEqual(['praat', 'giga', 'kokaia'], nrm.tokenize('praat giga kokaia'))

    def test_tokenize_empty(self):
        self.assertEqual([], nrm.tokenize(''))

    def test_remove_stopwords(self):
        self.assertEqual({'giga', 'roinis', 'kokaia'}, nrm.remove_stopwords('mr giga roinis dze kokaia'.split()))

    def test_normalize_and_tokenize(self):
        self.assertEqual({'giga', 'roinis', 'kokaia'}, nrm.normalize_and_tokenize('Mr.  Giga  (როინის ძე)  Kokaia. გიგა'))


if __name__ == '__main__':
    unittest.main()
