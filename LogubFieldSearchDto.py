from com.logub.logcontroller.api.schema import LogubFieldTypeDto
from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Data
from lombok import NoArgsConstructor

Java annotations have no direct Python equivalent:
#ORIGINAL LINE:
@Data @AllArgsConstructor @NoArgsConstructor @Builder(toBuilder = true) public class LogubFieldSearchDto
class LogubFieldSearchDto:

    def __init__(self):
        self.__type = com.logub.logcontroller.api.schema.LogubFieldTypeDto.Tag
        self.__name = None
        self.__values = None
        self.__negation = False
