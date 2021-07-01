from socket import *
import sys
import json
import logging
import logs.server_log_config

from utils import configs, send_message, get_message

CONFIGS = configs()
SERVER_LOGGER = logging.getLogger('server')


def handle_message(message):
    if CONFIGS.get('ACTION') in message \
            and message[CONFIGS.get('ACTION')] == CONFIGS.get('PRESENCE') \
            and CONFIGS.get('TIME') in message \
            and CONFIGS.get('USER') in message \
            and message[CONFIGS.get('USER')][CONFIGS.get('ACCOUNT_NAME')] == 'Guest':
        SERVER_LOGGER.info('Клиенту сформировано успешное сообщение')
        return {CONFIGS.get('RESPONSE'): 200}
    SERVER_LOGGER.critical('Клиенту сформировано сообщение об ошибке')
    return {
        CONFIGS.get('RESPONSE'): 400,
        CONFIGS.get('ERROR'): 'Bad Request'
    }


def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = CONFIGS.get('DEFAULT_PORT')
        if not 65535 >= listen_port >= 1024:
            raise ValueError
    except IndexError:
        SERVER_LOGGER.error('После -\'p\' необходимо указать порт')
        sys.exit(1)
    except ValueError:
        SERVER_LOGGER.error('Порт должен быть указан в пределах от 1024 до 65535')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
    except IndexError:
        SERVER_LOGGER.error('После -\'a\' необходимо указать адрес')
        sys.exit(1)

    transport = socket(AF_INET, SOCK_STREAM)
    transport.bind((listen_address, listen_port))
    transport.listen(CONFIGS.get('MAX_CONNECTIONS'))

    while True:
        client, client_address = transport.accept()
        try:
            message = get_message(client, CONFIGS)
            response = handle_message(message)
            send_message(client, response, CONFIGS)
            SERVER_LOGGER.info(f'Получено сервисное сообщение о присутствии')
            client.close()
        except (ValueError, json.JSONDecodeError):
            SERVER_LOGGER.error('Принято некорретное сообщение от клиента')
            client.close()


if __name__ == '__main__':
    main()
