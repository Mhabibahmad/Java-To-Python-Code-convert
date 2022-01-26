from com.logub.logcontroller.domain.model import LogLevel
from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Data
from lombok import NoArgsConstructor
from org.springframework.data.annotation import Id
from org.springframework.data.redis.core import RedisHash


#ORIGINAL LINE: @Data @AllArgsConstructor @NoArgsConstructor @Builder(toBuilder = true) @RedisHash("log") public class RLogubLog implements java.io.Serializable
class RLogubLog:

    def __init__(self):
     
        self.__id = str(java.util.UUID.randomUUID())
        self.__index = "principal"
        self.__systemProperties = None
        self.__businessProperties = None
        self.__message = None
        self.__timestamp = java.time.Instant.now().toEpochMilli()
        self.__service = None
        self.__logger = None
        self.__thread = None
        self.__source = None
        self.__level = None
