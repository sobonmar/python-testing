# Mock z parametrem spec - ograniczanie dostępnych atrybutów
import unittest
from unittest.mock import Mock

from main import len_joke


class JokeAPI:
    """Przykładowa klasa API do mockowania"""

    def fetch_joke(self):
        return "Chuck Norris joke"

    def get_status(self):
        return "OK"


class TestJokeAPIWithSpec(unittest.TestCase):
    def test_len_function(self):
        api_mock = Mock(spec=JokeAPI)
        api_mock.get_joke.return_value = "test jock"  # to zwróci błąd dokąd mamy spec

        result = len_joke(api_mock.get_joke)
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
