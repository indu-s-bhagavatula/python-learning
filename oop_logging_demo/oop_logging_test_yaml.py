import logging
import logging.config
import yaml

log_config_path="logging.yaml"
with open(log_config_path, 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

# create logger for application
app_logger = logging.getLogger("oop_logging_app")

app_logger.debug("This is a debug message")
app_logger.info("This is a info message")
