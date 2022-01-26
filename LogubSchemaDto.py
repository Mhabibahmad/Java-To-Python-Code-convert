from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Data
from lombok import NoArgsConstructor

 Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Data @AllArgsConstructor @NoArgsConstructor @Builder(toBuilder = true) public class LogubSchemaDto
class LogubSchemaDto:

    def __init__(self):
        self.__schema = None
