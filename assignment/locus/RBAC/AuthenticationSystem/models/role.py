"""
Base model class for Role
"""
from AuthenticationSystem.models.action_types import ActionTypes
from AuthenticationSystem.models.resources import Resources

class RoleModel():
    def __init__(self, name:str, resource:Resources, action_type:ActionTypes):
        """ Creates a new role with given role name and its corresponding usage rights
            :param name : name as string is the name of the role
            :param resource : resource as Resources
            :param action_type : action_type as ActionTypes
        """
        self.__name = name
        self.__resource = resource
        self.__action_type = action_type

    @property
    def name(self):
        return self.__name

    @property
    def resource(self):
        return self.__resource

    @property
    def action_type(self):
        return self.__action_type