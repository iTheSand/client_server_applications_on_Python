import logging
from logging import handlers
import sys
import os

sys.path.append('../')

SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

# STREAM_HANDLER = logging.StreamHandler(sys.stderr)
# STREAM_HANDLER.setFormatter(SERVER_FORMATTER)
# STREAM_HANDLER.setLevel(logging.ERROR)
# LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='D')
# LOG_FILE.setFormatter(SERVER_FORMATTER)
#
# LOGGER = logging.getLogger('server')
# LOGGER.addHandler(STREAM_HANDLER)
# LOGGER.addHandler(LOG_FILE)
# LOGGER.setLevel(logging.DEBUG)

SERVER_LOG = logging.getLogger('server')
SERVER_LOG.setLevel(logging.DEBUG)
# SERVER_FILE_HANDLER = logging.FileHandler(PATH, encoding='utf-8')
SERVER_FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='D')
SERVER_FILE_HANDLER.setFormatter(SERVER_FORMATTER)
SERVER_LOG.addHandler(SERVER_FILE_HANDLER)

if __name__ == '__main__':
    SERVER_LOG.debug('debug massage')
    SERVER_LOG.info('info massage')
    SERVER_LOG.warning('warning massage')
    SERVER_LOG.error('error massage')
    SERVER_LOG.critical('critical massage')
