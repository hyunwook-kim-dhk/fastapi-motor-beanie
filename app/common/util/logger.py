import logging
from enum import Enum
from logging import Formatter

LOG_FORMAT = "%(asctime)s %(name)s %(funcName)s %(levelname)s %(message)s"


class LogLevel(int, Enum):
    CRITICAL = logging.CRITICAL
    FATAL = logging.FATAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    WARN = logging.WARN
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    NOTSET = logging.NOTSET


def setup_logger(log_level: LogLevel) -> None:
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(Formatter(LOG_FORMAT))
    stream_handler.setLevel(log_level.value)
