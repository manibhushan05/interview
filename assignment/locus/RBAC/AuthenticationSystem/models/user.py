"""
Base model class for User
"""

class UserModel():
    def __init__(self, name:str, roles:list):
        """ Creates a user with given name and role
            :param name : name as string is the user name
            :param role : role as list of role
        """
        self.__name = name
        self.__roles = roles

    @property
    def name(self):
        return self.__name

    @property
    def roles(self):
        return self.__roles