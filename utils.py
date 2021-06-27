import json


def configs():
    CONFIGS = {
        "DEFAULT_IP_ADDRESS": "192.168.0.107",
        "DEFAULT_PORT": 7777,
        "MAX_CONNECTIONS": 5,
        "MAX_PACKAGE_LENGTH": 1024,
        "ENCODING": "utf-8",
        "ACTION": "action",
        "TIME": "time",
        "USER": "user",
        "ACCOUNT_NAME": "account_name",
        "PRESENCE": "presence",
        "RESPONSE": "response",
        "ERROR": "error"
    }
    return CONFIGS


def send_message(opened_socket, message, CONFIGS):
    json_message = json.dumps(message)
    response = json_message.encode(CONFIGS.get('ENCODING'))
    opened_socket.send(response)
    return response


def get_message(opened_socket, CONFIGS):
    response = opened_socket.recv(CONFIGS.get('MAX_PACKAGE_LENGTH'))
    if isinstance(response, bytes):
        json_response = response.decode(CONFIGS.get('ENCODING'))
        response_dict = json.loads(json_response)
        if isinstance(response_dict, dict):
            return response_dict
        raise ValueError
    raise ValueError
