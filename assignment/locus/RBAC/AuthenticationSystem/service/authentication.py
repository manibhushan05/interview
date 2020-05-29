from AuthenticationSystem.handlers.entity.user import UsersEntityHandler
from AuthenticationSystem.models.action_types import ActionTypes
from AuthenticationSystem.models.resources import Resources
from AuthenticationSystem.handlers.log import LogHandler
from AuthenticationSystem.handlers.validation import ValidationHandler

class AuthenticationService():
    def __init__(self):
        self.__logger = LogHandler.get_logger(__name__)
        self.__users = UsersEntityHandler().get()

    def authenticate(self, user:str, action_type:ActionTypes, resource:Resources):
        """ Method to authenticate user inputs as per available roles
            :param user : user as string is the logged_in user
            :param action_type : action_type as ActionType is the action which the logged_in user wants to perform
            :param resource : resource as Resources is the resource on which the logged_in user wants to perform action_type
            :return is_authenticated : is_authenticated as boolean is the authentication status
        """

        #validating user inputs
        ValidationHandler().validate_user_input(self.__users.keys(), user, action_type, resource)

        # getting all user roles
        user_roles = self.__users[user]

        # looping and creating a list valid actions as per roles
        valid_actions_for_resource = [role.name for role in user_roles if role.resource == resource and role.action_type == action_type]

        #if valid action is present means user is authenticated else false
        authtication_status = True if valid_actions_for_resource else False

        self.__logger.info('Authentication status for user "{}" to perform action "{}" in resource "{}" is "{}"'.format(user, action_type.value, resource.value, authtication_status))
        return authtication_status


