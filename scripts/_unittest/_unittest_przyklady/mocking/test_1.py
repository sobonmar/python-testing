# Stub
# unittest.mock.Mock
import unittest
from unittest.mock import Mock

from main import len_joke


class TestLenJoke(unittest.TestCase):
    def test_len_joke(self):
        get_joke_mock = Mock()
        get_joke_mock.return_value = "A super joke!"

        joke_length = len_joke(get_joke_mock)

        self.assertEqual(joke_length, 13)


if __name__ == "__main__":
    unittest.main()
