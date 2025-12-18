# Stub
# unittest.mock.MagicMock
import unittest
from unittest.mock import MagicMock

from main import len_joke


class TestLenJoke(unittest.TestCase):
    def test_len_joke(self):
        get_joke_mock = MagicMock()

        joke_length = len_joke(get_joke_mock)

        self.assertEqual(joke_length, 0)

if __name__ == "__main__":
    unittest.main()
