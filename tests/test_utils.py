import sys
import os
import unittest
import json
import time
from socket import *

sys.path.append('../')

from utils import configs, send_message, get_message
from client import create_presence_message


# sys.path.append(os.path.join(os.getcwd(), '...'))

# тестирование сокетов
# class TestSocket:
#     CONFIGS = configs()
#
#     def __init__(self, test_message):
#         self.test_message = test_message
#         self.encoded_message = None
#         self.received_message = None
#
#     def send(self, message_to_send):
#         json_test_message = json.dumps(self.test_message)
#         self.encoded_message = json_test_message.encode(self.CONFIGS["ENCODING"])
#         self.received_message = message_to_send
#
#     def recv(self, max_len):
#         json_test_message = json.dumps(self.test_message)
#         return json_test_message.encode(self.CONFIGS["ENCODING"])


class TestUtils(unittest.TestCase):
    CONFIGS = configs()
    server_address = CONFIGS.get('DEFAULT_IP_ADDRESS')
    server_port = CONFIGS.get('DEFAULT_PORT')

    # test_message_send = {
    #     CONFIGS.get('ACTION'): CONFIGS.get('PRESENCE'),
    #     CONFIGS.get('TIME'): time.time(),
    #     CONFIGS.get('USER'): {
    #         CONFIGS.get('ACCOUNT_NAME'): 'test_t'
    #     }
    # }
    #
    # test_success_receive = {CONFIGS["RESPONSE"]: 200}
    # test_error_receive = {
    #     CONFIGS['RESPONSE']: 400,
    #     CONFIGS['ERROR']: 'Bad Request'
    # }

    def test_type_data_send_message(self):
        message = create_presence_message('Guest')
        transport = socket(AF_INET, SOCK_STREAM)
        transport.connect((self.server_address, self.server_port))
        self.assertEqual(type(send_message(transport, message, CONFIGS=self.CONFIGS)), bytes)

    # def test_sock_get_message(self):
    #     test_sock_ok = TestSocket(self.test_success_receive)
    #     test_sock_err = TestSocket(self.test_error_receive)
    #     self.assertEqual(get_message(test_sock_ok, self.CONFIGS), self.test_success_receive)
    #     self.assertEqual(get_message(test_sock_err, self.CONFIGS), self.test_error_receive)


if __name__ == '__main__':
    unittest.main()
