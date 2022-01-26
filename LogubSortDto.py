from enum import Enum

from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Data
from lombok import NoArgsConstructor

 Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Data @AllArgsConstructor @NoArgsConstructor @Builder(toBuilder = true) public class LogubSortDto
class LogubSortDto:

    def __init__(self):
        #instance fields found 
        self.__field = None
        self.__order = 0

    class LogubOrderDto(Enum):
        ASC = 0
        DESC = 1
