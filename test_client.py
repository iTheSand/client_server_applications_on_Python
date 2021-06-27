import unittest
import time

from client import create_presence_message, handle_response
from utils import configs


class TestClient(unittest.TestCase):
    CONFIGS = configs()

    def test_create_presence(self):
        message = create_presence_message('Guest')
        self.assertEqual(
            message,
            {
                self.CONFIGS.get('ACTION'): self.CONFIGS.get('PRESENCE'),
                self.CONFIGS.get('TIME'): time.time(),
                self.CONFIGS.get('USER'): {
                    self.CONFIGS.get('ACCOUNT_NAME'): 'Guest'
                }
            }
        )

    def test_correct_handle_response_ok(self):
        response = {self.CONFIGS['RESPONSE']: 200}
        self.assertEqual(handle_response(response), '200 : OK')

    def test_correct_handle_response_error(self):
        response = {
            self.CONFIGS['RESPONSE']: 400,
            self.CONFIGS['ERROR']: 'Bad Request'
        }
        self.assertEqual(handle_response(response), '400 : Bad Request')

    def test_no_correct_handle_response(self):
        response = {self.CONFIGS['ERROR']: 'Bad Request'}
        self.assertRaises(ValueError, handle_response, response)


if __name__ == '__main__':
    unittest.main()
