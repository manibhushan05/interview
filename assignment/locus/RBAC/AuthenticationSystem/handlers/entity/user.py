from AuthenticationSystem.models.user import UserModel
from AuthenticationSystem.handlers.entity import EntityHandler
from AuthenticationSystem.handlers.entity.role import RoleEntityHandler

class UsersEntityHandler(EntityHandler):
    """ Class to handle user activity like creating a collection of users and exposing those
    """

    def __init__(self):
        """ Constructor which creates a collection of users with corresponding roles
        """
        super().__init__()
        self.__users = {}
        self._populate_default_entity()

    def _populate_default_entity(self):
        """ Private method to populate users and corresponding roles
        """
        available_roles = RoleEntityHandler().get()
        available_users = []
        available_users.append(UserModel(name='sysadmin', roles=[role for role in available_roles]))                                                            # sysadmin user with all available roles for all atrributes and resources
        available_users.append(UserModel(name='admin', roles=[role for role in available_roles if int(role.name[-1]) % 3 == 1 or int(role.name[-1]) % 3 == 2])) # admin user with read & write roles for all resources
        available_users.append(UserModel(name='device_admin', roles=[role for role in available_roles if int(role.name[-1]) > 0 and int(role.name[-1]) < 4]))   # device_admin user with all roles for only device_management resource
        available_users.append(UserModel(name='dashboard_admin', roles=[role for role in available_roles if int(role.name[-1]) > 3 and int(role.name[-1]) < 7]))# dashboard_admin user with all roles for only dashboard resource
        available_users.append(UserModel(name='system_admin', roles=[role for role in available_roles if int(role.name[-1]) > 6 and int(role.name[-1]) < 10]))  # system_admin user with all roles for only administration resource
        available_users.append(UserModel(name='random_1', roles=[role for role in available_roles if int(role.name[-1]) in [1,3,7,8]]))  # a random user with role r1, r3, r7 and r8
        
        # you can add a new user here

        #converting the list of users to dictionary for ease of use
        for user in available_users:
            self.__users.update({user.name: user.roles})
        

    def get(self):
        """ Public method to exposing all a collection of pre-created users with roles
            :return self.__users : self.__roles as collection of users with corresponding roles
        """
        return self.__users

