from abc import ABC, abstractmethod

class EntityHandler(ABC):
    """ Abstract entity handler class which needs to be implemented by child entity classes
    """

    def __init__(self):
        pass

    @abstractmethod
    def _populate_default_entity(self):
        pass

    @abstractmethod
    def get(self):
        pass
