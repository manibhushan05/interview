from enum import Enum

class ActionTypes(Enum):
    READ = 'READ'
    WRITE = 'WRITE'
    DELETE = 'DELETE'