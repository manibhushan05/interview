from AuthenticationSystem.models.action_types import ActionTypes
from AuthenticationSystem.models.resources import Resources
from AuthenticationSystem.handlers.log import LogHandler
import AuthenticationSystem.handlers.exception as ExceptionHandler

class ValidationHandler():
    """ Validation class """
    def __init__(self):
        self.__logger = LogHandler.get_logger(__name__)

    def validate_user_input(self, all_users:list, user:str, action_type:ActionTypes, resource:Resources):
        """ Method to validate user inputs
            :param user : user as string is the logged_in user
            :param action_type : action_type as ActionType is the action which the logged_in user wants to perform
            :param resource : resource as Resources is the resource on which the logged_in user wants to perform action_type
        """
        self.__logger.debug('Validating user inputs')

        if not user or not action_type or not resource:
            raise ExceptionHandler.NoneValueException(value_type="entity")

        if user not in all_users:
            raise ExceptionHandler.MissingUserException(user)

        if action_type not in ActionTypes:
            raise ExceptionHandler.MissingActionTypeException(action_type)

        if resource not in Resources:
            raise ExceptionHandler.MissingResourcesException(resource)

        self.__logger.info('Input user data are valid')