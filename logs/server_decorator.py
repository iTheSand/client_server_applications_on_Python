import logging
import inspect

SERVER_LOGGER = logging.getLogger('server')


def trace(func):
    def wrapper(*args, **kwargs):
        SERVER_LOGGER.debug(f'Имя функции - {func.__name__}; ' 
                            f'Аргументы функции - {args} & {kwargs}; '
                            f'Функция - {func.__name__} вызвана из функции - {inspect.stack()[1][3]}')
        r = func(*args, **kwargs)
        return r

    return wrapper
