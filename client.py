from socket import *
import sys
import time
import json
import logging
import logs.client_log_config
from logs.client_decorator import Trace

from utils import configs, send_message, get_message

CONFIGS = configs()
CLIENT_LOGGER = logging.getLogger('client')


@Trace()
def create_presence_message(account_name):
    message = {
        CONFIGS.get('ACTION'): CONFIGS.get('PRESENCE'),
        CONFIGS.get('TIME'): time.time(),
        CONFIGS.get('USER'): {
            CONFIGS.get('ACCOUNT_NAME'): account_name
        }
    }
    CLIENT_LOGGER.info('Создание сообщения для отправки на сервер')
    return message


@Trace()
def handle_response(message):
    CLIENT_LOGGER.info('Обработка сообщения от сервера')
    if CONFIGS.get('RESPONSE') in message:
        if message[CONFIGS.get('RESPONSE')] == 200:
            CLIENT_LOGGER.info('Успешная обработка сообщения от сервера')
            return '200 : OK'
        CLIENT_LOGGER.error('Неудачная обработка сообщения от сервера')
        return f'400 : {message[CONFIGS.get("ERROR")]}'
    raise ValueError


@Trace()
def main():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if not 65535 >= server_port >= 1024:
            raise ValueError
    except IndexError:
        CLIENT_LOGGER.warning('Установлены дефолтные значения ip адреса и порта')
        server_address = CONFIGS.get('DEFAULT_IP_ADDRESS')
        server_port = CONFIGS.get('DEFAULT_PORT')
    except ValueError:
        CLIENT_LOGGER.critical('Порт должен быть указан в пределах от 1024 до 65535')
        sys.exit(1)

    transport = socket(AF_INET, SOCK_STREAM)
    try:
        transport.connect((server_address, server_port))
    except ConnectionRefusedError:
        CLIENT_LOGGER.critical('Подключение недоступно!')

    presence_message = create_presence_message('Guest')
    CLIENT_LOGGER.info('Отправка сообщения серверу')
    send_message(transport, presence_message, CONFIGS)
    try:
        response = get_message(transport, CONFIGS)
        CLIENT_LOGGER.info(f'Сообщение от сервера: {response}')
        CLIENT_LOGGER.info(f'Ответ от сервера: {handle_response(response)}')
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOGGER.critical('Ошибка декодирования сообщения')


if __name__ == '__main__':
    main()
