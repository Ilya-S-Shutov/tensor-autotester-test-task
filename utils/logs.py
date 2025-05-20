import logging
from functools import wraps


def log_selenium_actions(func):
    logger_name = 'myLogger'

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(logger_name)

        class_name = args[0].__class__.__name__ if args else ''
        logger.info(f"Executing: {class_name}.{func.__name__}")

        try:
            result = func(*args, **kwargs)
            logger.info(f"Completed: {class_name}.{func.__name__}")
            return result
        except Exception as e:
            logger.error(f"Failed: {class_name}.{func.__name__} - {str(e)}")
            raise

    return wrapper