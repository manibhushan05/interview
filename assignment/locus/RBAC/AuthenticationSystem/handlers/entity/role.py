from AuthenticationSystem.models.action_types import ActionTypes
from AuthenticationSystem.models.resources import Resources
from AuthenticationSystem.models.role import RoleModel
from AuthenticationSystem.handlers.entity import EntityHandler

class RoleEntityHandler(EntityHandler):
    """ Class to handles roles activity like populating default roles and exposing the roles
    """

    def __init__(self):
        """ Constructor which creates default list of roles from available Resources & ActionType
        """
        super().__init__()
        self.__roles = []
        self._populate_default_entity()

    def _populate_default_entity(self):
        """ Private method to populate roles based on Resources & ActionType. For each Resouce, N actionType are created where N is the number of actionType
        """
        role_counter = 1
        for current_resource in Resources:
            for current_action_type in ActionTypes:
                self.__roles.append(RoleModel(name='r{}'.format(role_counter), resource=current_resource, action_type=current_action_type))
                role_counter += 1

    def get(self):
        """ Public method to exposing all availables to others
            :return self.__roles : self.__roles as list of roles
        """
        return self.__roles
