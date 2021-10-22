import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s %(message)s',
                    datefmt='%m/%d/%Y')

logging.debug("Debug log")
logging.info("info log")
logging.warning("warning log")
logging.error("error log")
logging.critical("critical log")

import logging_main_impl