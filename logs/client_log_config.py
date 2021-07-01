import logging
import sys
import os

sys.path.append('../')

CLIENT_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')

# STREAM_HANDLER = logging.StreamHandler(sys.stderr)
# STREAM_HANDLER.setFormatter(CLIENT_FORMATTER)
# STREAM_HANDLER.setLevel(logging.ERROR)
# LOG_FILE = logging.FileHandler(PATH, encoding='utf-8')
# LOG_FILE.setFormatter(CLIENT_FORMATTER)
#
# LOGGER = logging.getLogger('client')
# LOGGER.addHandler(STREAM_HANDLER)
# LOGGER.addHandler(LOG_FILE)
# LOGGER.setLevel(logging.DEBUG)

CLIENT_LOG = logging.getLogger('client')
CLIENT_LOG.setLevel(logging.DEBUG)
CLIENT_FILE_HANDLER = logging.FileHandler(PATH, encoding='utf-8')
CLIENT_FILE_HANDLER.setFormatter(CLIENT_FORMATTER)
CLIENT_LOG.addHandler(CLIENT_FILE_HANDLER)

if __name__ == '__main__':
    CLIENT_LOG.debug('debug massage')
    CLIENT_LOG.info('info massage')
    CLIENT_LOG.warning('warning massage')
    CLIENT_LOG.error('error massage')
    CLIENT_LOG.critical('critical massage')
