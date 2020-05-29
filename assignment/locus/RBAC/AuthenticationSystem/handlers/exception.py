from AuthenticationSystem.handlers.log import LogHandler

class AuthenticationSystemExceptionHandler(Exception):
    """ Base exception class for this application """
    def __init__(self):
        self.exception_logger = LogHandler.get_logger(__name__)

class MissingEntityException(AuthenticationSystemExceptionHandler):
    """ Base exception class for missing entities, inherits from AuthenticationSystemExceptionHandler"""
    def __init__(self, entity_type, missing_value):
        super().__init__()
        self.exception_logger.critical('{} {} does not exists in the system'.format(entity_type, missing_value))

class MissingUserException(MissingEntityException):
    """ Exception handler for missing users """
    def __init__(self, missing_value):
        super().__init__('User', missing_value)

class MissingResourcesException(MissingEntityException):
    """ Exception handler for missing resourcs """
    def __init__(self, missing_value):
        super().__init__('Resource', missing_value)

class MissingActionTypeException(MissingEntityException):
    """ Exception handler for missing action-type """
    def __init__(self, missing_value):
        super().__init__('ActionType', missing_value)

class NoneValueException(AuthenticationSystemExceptionHandler):
    """ Exception when None value is detected"""
    def __init__(self, value_type = None):
        super().__init__()
        self.exception_logger.critical('None value received {}.'.format('for {}'.format(value_type) if value_type else ''))