from enum import Enum

from lombok import AllArgsConstructor
from lombok import NoArgsConstructor

class LogLevel(Enum):
    INFO = 0
    DEBUG = 1
    ERROR = 2
    WARN = 3
    FATAL = 4
    UNKNOWN = 5
