from loguru import logger

# Configure logging with loguru
logger.add('system_logs.log', level='INFO', rotation='1 week', compression='zip')

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
