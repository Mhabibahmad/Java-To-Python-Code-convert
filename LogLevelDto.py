from enum import Enum

class LogLevelDto(Enum):
    INFO = 0
    DEBUG = 1
    ERROR = 2
    WARN = 3
    FATAL = 4
    UNKNOWN = 5
