import logging.config


def initlogger(path="logger.conf"):
    logging.config.fileConfig(path)
