import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter(
    fmt='%(asctime)s | %(name) -10s | %(levelname) -8s - %(message)s',
    datefmt='%Y/%m/%d %H:%M:%S')

# StreamHandler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# FileHandler
file_handler = logging.FileHandler('output.log', encoding='utf-8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def main():
    logger.info('这是一条中文消息')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    logger.info('Finish')
    logger.debug('Hello %s, %s!' % ('World', 'Congratulations'))


if __name__ == '__main__':
    main()
