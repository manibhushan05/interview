from logging.handlers import RotatingFileHandler
import logging

class LogHandler():
    """ Class for handling logs
    """
    def __init__(self):
        pass

    @staticmethod
    def get_logger(logger_name:str):
        """ Static class to get a file for logging exception message
            :param logger_name : logger_name as string is the expected name of the logger
        """
        if logger_name:

            if len(logger_name.strip()) == 0:
                return logging.getLogger()

            logger = logging.getLogger(logger_name)
            log_formatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
                        
            logger.setLevel(logging.INFO)
            if not logger.hasHandlers():
                file_log_handler = RotatingFileHandler(filename='auth_system.log', maxBytes=10*1024*1024, backupCount=10)
                file_log_handler.setFormatter(log_formatter)
                logger.addHandler(file_log_handler)
            return logger