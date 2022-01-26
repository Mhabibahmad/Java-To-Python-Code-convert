
#import static com.logub.logcontroller.domain.model.LogLevel.UNKNOWN

#import static lombok.AccessLevel.PRIVATE

from lombok import AllArgsConstructor
from lombok import Builder
from lombok import NonNull
from lombok import Value


#ORIGINAL LINE: @Value @AllArgsConstructor(access = PRIVATE) @Builder(toBuilder = true) public class LogubLog
class LogubLog:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__id = str(java.util.UUID.randomUUID())
        self.__index = "principal"
        self.__systemProperties = None
        self.__businessProperties = java.util.Collections.emptyMap()
        self.__message = java.util.Optional.empty()
        self.__timestamp = java.time.Instant.now()
        self.__service = java.util.Optional.empty()
        self.__logger = java.util.Optional.empty()
        self.__thread = java.util.Optional.empty()
        self.__source = java.util.Optional.empty()
        self.__level = UNKNOWN
