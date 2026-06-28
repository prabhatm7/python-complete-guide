import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a rotating file handler
handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
formatter = logging.Formatter('%(asctime)s [ %(levelname)s ] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

for _ in range(1000):
    logger.info("This is a log message that will be rotated.")