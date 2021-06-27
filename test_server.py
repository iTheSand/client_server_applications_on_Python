import unittest
import time

from server import handle_message
from utils import configs


class TestServer(unittest.TestCase):
    CONFIGS = configs()

    success_message = {CONFIGS['RESPONSE']: 200}

    error_message = {
        CONFIGS['RESPONSE']: 400,
        CONFIGS['ERROR']: 'Bad Request'
    }

    def test_without_action(self):
        self.assertEqual(
            handle_message({
                self.CONFIGS['TIME']: 1.1,
                self.CONFIGS['USER']: {
                    self.CONFIGS['ACCOUNT_NAME']: 'Guest'
                }
            }), self.error_message)

    def test_no_success_data(self):
        self.assertEqual(
            handle_message({
                self.CONFIGS['ACTION']: self.CONFIGS['RESPONSE'],
                self.CONFIGS.get('TIME'): time.time(),
                self.CONFIGS.get('USER'): {
                    self.CONFIGS.get('ACCOUNT_NAME'): 'Guest',
                }
            }), self.error_message)

    def test_success_data(self):
        self.assertEqual(
            handle_message({
                self.CONFIGS['ACTION']: self.CONFIGS['PRESENCE'],
                self.CONFIGS.get('TIME'): time.time(),
                self.CONFIGS.get('USER'): {
                    self.CONFIGS.get('ACCOUNT_NAME'): 'Guest',
                }
            }), self.success_message)


if __name__ == '__main__':
    unittest.main()
