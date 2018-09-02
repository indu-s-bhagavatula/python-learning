import logging
import logging.config

# Refer logging settings from config file
logging.config.fileConfig("logging.conf")

# create logger for application
app_logger = logging.getLogger("oop_logging_app")

app_logger.debug("This is a debug message")
app_logger.info("This is a info message")
