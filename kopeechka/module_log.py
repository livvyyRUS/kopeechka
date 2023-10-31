import logging
import sys


class Logger:
    def __init__(self, level: int = logging.DEBUG, handler: logging.Handler = logging.StreamHandler(stream=sys.stdout), format_string: str = "%(levelname)s | %(lineno)d | %(pathname)s | %(message)s"):
        self.logger = logging.Logger("kopeechka")

        self.logger.setLevel(level)
        formatter = logging.Formatter(format_string)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, level: int = logging.DEBUG, msg: str = ""):
        self.logger.log(level, msg)

    def debug(self, msg: str = ""):
        self.logger.debug(msg)

    def info(self, msg: str = ""):
        self.logger.info(msg)

    def warning(self, msg: str = ""):
        self.logger.warning(msg)

    def error(self, msg: str = ""):
        self.logger.error(msg)

    def critical(self, msg: str = ""):
        self.logger.critical(msg)

    def change_settings(self, level: int = logging.DEBUG, handler: logging.Handler = logging.StreamHandler(stream=sys.stdout), format_string: str = "%(levelname)s | %(lineno)d | %(pathname)s | %(message)s"):
        self.logger = logging.Logger("kopeechka")

        self.logger.setLevel(level)
        formatter = logging.Formatter(format_string)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
