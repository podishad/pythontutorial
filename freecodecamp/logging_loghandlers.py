import logging

logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# set formatter
formatter_set = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s %(message)s')
stream_h.setFormatter(formatter_set)
file_h.setFormatter(formatter_set)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("THIS IS A WARNING")
logger.error("THIS IS AN ERROR")
