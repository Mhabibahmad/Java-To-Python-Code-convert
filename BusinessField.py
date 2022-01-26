
#import static lombok.AccessLevel.PRIVATE

from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Data
from lombok import NoArgsConstructor
from lombok import Value

#ORIGINAL LINE: @Value @AllArgsConstructor(access = PRIVATE) @Builder(toBuilder = true) public class BusinessField
class BusinessField:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__type = None
        self.__name = None
