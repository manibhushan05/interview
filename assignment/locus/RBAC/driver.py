import AuthenticationSystem
from AuthenticationSystem.handlers.entity.user import UsersEntityHandler
from AuthenticationSystem.service.authentication import AuthenticationService
import sys
import traceback

class Driver():
    """ Driver class for driving the Authentication System 
    """
    def __init__(self):
        self.__all_users = UsersEntityHandler().get()

    def get_input_choice(self, message:str, choices:list):
        """ Method to get user inputs via console
            :param message : message as string is the prompt message
            :param choices : choices as list of valid integers which user can enter
            :return user_choice : user_choice as integer which user has selected
        """
        user_choice = 0
        while user_choice not in choices:
            try:
                user_choice = int(input('{}: '.format(message)))
            except ValueError:
                user_choice = 0
        return user_choice

    def show_role_chart(self):
        """ Method to show the chat of users, resources and action-type
        """
        print('\n{} -> {} -> {}'.format('USER'.ljust(15), 'RESOURCES'.ljust(20), 'ACTION-TYPE'))
        for user, roles in self.__all_users.items():
            [print('{} -> {} -> {}'.format(user.ljust(15), str(role.resource.value).ljust(20), role.action_type.value)) for role in roles]
        print('\n')

    def choose_user(self):
        """ Method to show list of users and get the user selected resource
        """
        selected_user = None
        print('Following are the list of available users')
        for index, user in enumerate(self.__all_users.keys()):
            print('\t\t\t{}. {}'.format(index + 1, user))
        user_choice = self.get_input_choice('Choose a user', range(1, len(self.__all_users.keys()) + 1))
        for index, user in enumerate(self.__all_users.keys()):
            if index +1 == user_choice:
                selected_user = user
                break
        return selected_user

    def choose_resource(self):
        """ Method to show list of resource and get the user selected resource
        """
        selected_resource = None
        print('Following are the list of available resources :')
        for index, resource in enumerate(AuthenticationSystem.models.resources.Resources):
            print('\t\t{}. {}'.format(index + 1, resource.value))
        user_choice = self.get_input_choice('Choose a resource', range(1, len(AuthenticationSystem.models.resources.Resources) + 1))
        for index, resource in enumerate(AuthenticationSystem.models.resources.Resources):
            if index +1 == user_choice:
                selected_resource = resource
                break
        return selected_resource
        
    def choose_action_type(self):
        """ Method to show list of action-type and get the user selected action-type
        """
        selected_action_type = None
        print('Following are the list of available action-types :')
        for index, action_type in enumerate(AuthenticationSystem.models.action_types.ActionTypes):
            print('\t\t{}. {}'.format(index + 1, action_type.value))
        user_choice = self.get_input_choice('Choose an action-type', range(1, len(AuthenticationSystem.models.action_types.ActionTypes) + 1))
        for index, action_type in enumerate(AuthenticationSystem.models.action_types.ActionTypes):
            if index +1 == user_choice:
                selected_action_type = action_type
                break
        return selected_action_type


## main function
if __name__ == "__main__":
    try:
        driver = Driver()
        driver.show_role_chart()                        # displaying the role-chart
        selected_user = driver.choose_user()            # getting user-input
        selected_resource = driver.choose_resource()    # getting user-input
        selected_action = driver.choose_action_type()   # getting user-input

        #Calling authenticate method inside to AuthenticationService to check user 
        print('\nAuthentication status = {}'.format(AuthenticationService().authenticate(selected_user, selected_action, selected_resource)))
    except:
        print('-'*60)
        traceback.print_exc(file=sys.stdout)
        print('-'*60)