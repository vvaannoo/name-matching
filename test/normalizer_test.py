import unittest
from src import normalizer


class TestNormalizer(unittest.TestCase):

    def test_transliterate_geo(self):
        self.assertEqual(normalizer.transliterate('გიგა კოკაია.'), 'giga kokaia.')

    def test_transliterate_eng(self):
        self.assertEqual(normalizer.transliterate('Giga Kokaia.'), 'Giga Kokaia.')

    def test_transliterate_mixed(self):
        self.assertEqual(normalizer.transliterate('Giga კოკაია.'), 'Giga kokaia.')

    def test_transliterate_empty(self):
        self.assertIsNone(normalizer.transliterate(''))

    def test_transliterate_none(self):
        self.assertIsNone(normalizer.transliterate(None))

    def test_remove_symbols_1(self):
        self.assertEqual(normalizer.remove_symbols(' g.giga -kokaia!'), 'g giga kokaia')

    def test_remove_symbols_without_symbols(self):
        self.assertEqual(normalizer.remove_symbols('kokaia'), 'kokaia')

    def test_tokenize(self):
        self.assertEqual(normalizer.tokenize('praat giga kokaia'), ['praat', 'giga', 'kokaia'])

    def test_tokenize_empty(self):
        self.assertEqual(normalizer.tokenize(''), [])

    def test_remove_stopwords(self):
        self.assertEqual(normalizer.remove_stopwords('mr giga roinis dze kokaia'.split()), ['giga', 'roinis', 'kokaia'])

    def test_normalize_and_tokenize(self):
        self.assertEqual(normalizer.normalize_and_tokenize('Mr.  Giga  (როინის ძე)  Kokaia.'), ['giga', 'roinis', 'kokaia'])


if __name__ == '__main__':
    unittest.main()
