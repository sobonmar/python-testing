# pytest rozumie unittest.mock
import unittest

from unittest.mock import MagicMock, patch

from main import get_joke


class TestGetJoke(unittest.TestCase):

    @patch('main.requests')
    def test_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "value": "A super joke"
        }
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "A super joke")

    @patch('main.requests')
    def test_fail_get_joke(self, mock_requests):
        mock_response = MagicMock(status_code=300)
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "")


if __name__ == "__main__":
    unittest.main()
