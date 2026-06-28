import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [ %(levelname)s ] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")


try:
    a = {1, 2, 3}
    val = a[5]  # This will raise an IndexError
except IndexError as e:
    logger.error("An exception occurred: %s", e, exc_info=True)