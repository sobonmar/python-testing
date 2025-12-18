# Spy
# Mock z parametrem wraps - częściowe mockowanie
import unittest
from unittest.mock import Mock

from main import len_joke


class JokeAPI:
    """Przykładowa klasa API do mockowania"""

    def get_joke(self):
        return "Chuck Norris counted to infinity twice"

    def get_status(self):
        return "OK"

    def log_request(self):
        print("API request logged")


class TestJokeAPIWithWraps(unittest.TestCase):
    def test_len_function(self):
        spy = Mock(wraps=JokeAPI())

        result = len_joke(spy.get_joke)
        self.assertEqual(result, 38)

        spy.get_joke.assert_called_once()

        spy.get_status.return_value = "MOCKED"
        self.assertEqual(spy.get_status(), "MOCKED")


if __name__ == "__main__":
    unittest.main()
