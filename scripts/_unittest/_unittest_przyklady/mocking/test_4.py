# mocki a sprawdzanie wyjątków
import unittest
from unittest.mock import Mock

from requests.exceptions import Timeout

from main import len_joke



class TestLenJoke(unittest.TestCase):
    def test_len_joke_function_timeout_exception(self):
        get_joke_mock = Mock()
        get_joke_mock.side_effect = Timeout("Service unavailable")

        with self.assertRaises(Timeout):
           len_joke(get_joke_mock)

        get_joke_mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
