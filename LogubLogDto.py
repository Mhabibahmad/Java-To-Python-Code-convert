from com.logub.logcontroller.domain.model import SystemProperties
from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Data
from lombok import NoArgsConstructor


 Java annotations have no direct Python equivalent:
#ORIGINAL LINE: 
@Data @AllArgsConstructor @NoArgsConstructor @Builder(toBuilder = true) public class LogubLogDto
class LogubLogDto:

    def __init__(self):
        self.__id = str(java.util.UUID.randomUUID())
        self.__index = "principal"
        self.__systemProperties = None
        self.__businessProperties = None
        self.__message = java.util.Optional.empty()
        self.__timestamp = java.time.Instant.now()
        self.__service = java.util.Optional.empty()
        self.__logger = java.util.Optional.empty()
        self.__thread = java.util.Optional.empty()
        self.__source = java.util.Optional.empty()
        self.__level = None
