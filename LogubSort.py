from enum import Enum

#import static lombok.AccessLevel.PRIVATE

from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Value

#ORIGINAL LINE: @Value @AllArgsConstructor(access = PRIVATE) @Builder(toBuilder = true) public class LogubSort
class LogubSort:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__field = None
        self.__order = 0

    class LogubOrder(Enum):
        ASC = 0
        DESC = 1
