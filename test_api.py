from api import api
import unittest
from unittest.mock import MagicMock, patch


class TestAPI(unittest.TestCase):

    def test_API_1(self):
        mock_response = MagicMock()
        mock_response.json = MagicMock(return_value={"response": True, "size": "9",
                                                     "squares": [{"x": 0, "y": 1,
                                                                  "value": 6},
                                                                 {"x": 0, "y": 7,
                                                                  "value": 1},
                                                                 {"x": 0, "y": 8,
                                                                  "value": 2},
                                                                 {"x": 1, "y": 1,
                                                                  "value": 2},
                                                                 {"x": 1, "y": 4,
                                                                  "value": 3},
                                                                 {"x": 1, "y": 5,
                                                                  "value": 9},
                                                                 {"x": 1, "y": 7,
                                                                  "value": 5},
                                                                 {"x": 1, "y": 8,
                                                                  "value": 6},
                                                                 {"x": 2, "y": 1,
                                                                  "value": 7},
                                                                 {"x": 2, "y": 2,
                                                                  "value": 4},
                                                                 {"x": 2, "y": 5,
                                                                  "value": 6},
                                                                 {"x": 2, "y": 6,
                                                                  "value": 3},
                                                                 {"x": 3, "y": 0,
                                                                  "value": 4},
                                                                 {"x": 3, "y": 3,
                                                                  "value": 6},
                                                                 {"x": 3, "y": 4,
                                                                  "value": 2},
                                                                 {"x": 3, "y": 5,
                                                                  "value": 8},
                                                                 {"x": 3, "y": 8,
                                                                  "value": 9},
                                                                 {"x": 4, "y": 0,
                                                                  "value": 7},
                                                                 {"x": 4, "y": 2,
                                                                  "value": 6},
                                                                 {"x": 4, "y": 4,
                                                                  "value": 5},
                                                                 {"x": 4, "y": 6,
                                                                  "value": 2},
                                                                 {"x": 4, "y": 8,
                                                                  "value": 3},
                                                                 {"x": 5, "y": 0,
                                                                  "value": 9},
                                                                 {"x": 5, "y": 3,
                                                                  "value": 4},
                                                                 {"x": 5, "y": 8,
                                                                  "value": 5},
                                                                 {"x": 6, "y": 0,
                                                                  "value": 2},
                                                                 {"x": 6, "y": 2,
                                                                  "value": 5},
                                                                 {"x": 6, "y": 3,
                                                                  "value": 1},
                                                                 {"x": 6, "y": 6,
                                                                  "value": 9},
                                                                 {"x": 6, "y": 7,
                                                                  "value": 8},
                                                                 {"x": 7, "y": 1,
                                                                  "value": 9},
                                                                 {"x": 7, "y": 3,
                                                                  "value": 3},
                                                                 {"x": 7, "y": 4,
                                                                  "value": 8},
                                                                 {"x": 7, "y": 6,
                                                                  "value": 5},
                                                                 {"x": 7, "y": 7,
                                                                  "value": 2},
                                                                 {"x": 8, "y": 1,
                                                                  "value": 4},
                                                                 {"x": 8, "y": 2,
                                                                  "value": 1},
                                                                 {"x": 8, "y": 4,
                                                                  "value": 9},
                                                                 {"x": 8, "y": 6,
                                                                  "value": 6},
                                                                 {"x": 8, "y": 7,
                                                                  "value": 3}]})
        with patch("api.requests.get", return_value=mock_response):
            result = api(9)
        self.assertEqual(result, [[0, 0, 0, 4, 7, 9, 2, 0, 0],
                                  [6, 2, 7, 0, 0, 0, 0, 9, 4],
                                  [0, 0, 4, 0, 6, 0, 5, 0, 1],
                                  [0, 0, 0, 6, 0, 4, 1, 3, 0],
                                  [0, 3, 0, 2, 5, 0, 0, 8, 9],
                                  [0, 9, 6, 8, 0, 0, 0, 0, 0],
                                  [0, 0, 3, 0, 2, 0, 9, 5, 6],
                                  [1, 5, 0, 0, 0, 0, 8, 2, 3],
                                  [2, 6, 0, 9, 3, 5, 0, 0, 0]])


if __name__ == "__main__":
    unittest.main()
