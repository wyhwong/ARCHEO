import logging
import env

LOGFMT = "%(asctime)s [%(name)s | %(levelname)s]: %(message)s"
DATEFMT = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(format=LOGFMT, datefmt=DATEFMT, level=env.LOGLEVEL)


def get_logger(logger_name: str, log_filepath=env.LOGFILEPATH) -> logging.Logger:
    """
    Get a logger.

    Parameters
    ----------
    logger_name : str
        Name of the logger.
    log_filepath : str, optional
        Path to the log file.

    Returns
    -------
    logger : Logger
        Logger.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(env.LOGLEVEL)
    if log_filepath:
        handler = logging.FileHandler(filename=log_filepath)
        formatter = logging.Formatter(fmt=LOGFMT, datefmt=DATEFMT)
        handler.setFormatter(fmt=formatter)
        logger.addHandler(handler)
    return logger
