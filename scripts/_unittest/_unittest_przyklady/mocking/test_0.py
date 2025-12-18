# Dummy
import unittest

from main import len_joke


class TestLenJoke(unittest.TestCase):
    def test_len_joke(self):
        get_joke_mock = lambda: "A super joke!"
        joke_length = len_joke(get_joke_mock)
        self.assertEqual(joke_length, 13)


if __name__ == "__main__":
    unittest.main()
