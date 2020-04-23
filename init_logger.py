import logging
import sys

FORMAT_DISPLAY = '%(levelname) -7s - %(message)s'
FORMAT_LOG_FILE = '%(asctime)s | %(name)s | %(levelname) -7s - %(message)s'
FORMAT_DATETIME = '%Y/%m/%d %H:%M:%S'


class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    NO_COLOR = "\x1b[m"
    RED, GREEN, ORANGE, BLUE, PURPLE, LBLUE, GREY, WHITE = \
        map("\x1b[%dm".__mod__, range(31, 39))

    BOLD_RED = '\x1b[31;1m'

    format = FORMAT_DISPLAY

    FORMATS = {
        logging.DEBUG: BLUE + format + NO_COLOR,
        logging.INFO: WHITE + format + NO_COLOR,
        logging.WARNING: ORANGE + format + NO_COLOR,
        logging.ERROR: RED + format + NO_COLOR,
        logging.CRITICAL: BOLD_RED + format + NO_COLOR
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_my_logger(mod_name):
    logger = logging.getLogger(mod_name)
    logger.setLevel(level=logging.DEBUG)
    formatter_file = logging.Formatter(fmt=FORMAT_LOG_FILE, datefmt=FORMAT_DATETIME)

    # StreamHandler
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(CustomFormatter())
    logger.addHandler(stream_handler)

    # FileHandler
    file_handler = logging.FileHandler('output.log', encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter_file)
    logger.addHandler(file_handler)

    return logger
