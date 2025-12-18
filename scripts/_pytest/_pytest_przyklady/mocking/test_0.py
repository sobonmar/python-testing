# pytest rozumie unittest.mock
import unittest
from unittest.mock import MagicMock

from main import len_joke


class TestLenJoke(unittest.TestCase):
    def test_len_joke(self):
        get_joke_mock = MagicMock()

        res = len_joke(get_joke_mock)
        assert res == 0


if __name__ == "__main__":
    unittest.main()
