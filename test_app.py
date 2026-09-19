import unittest
from unittest.mock import patch
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    @patch("app.requests.get")
    def test_gists(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {
                "id": "123",
                "description": "test gist",
                "html_url": "https://gist.github.com/123"
            }
        ]

        response = self.client.get("/octocat")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json[0]["id"], "123")

    @patch("app.requests.get")
    def test_user_not_found(self, mock_get):
        mock_get.return_value.status_code = 404

        response = self.client.get("/does-not-exist")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "GitHub user not found")

if __name__ == "__main__":
    unittest.main()
