import unittest

class TestSomething(unittest.TestCase):
    def test_feature_one(self):
        # Votre test ici
        self.assertEqual('foo'.upper(), 'FOO')

    def test_feature_two(self):
        # Un autre test
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())