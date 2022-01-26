from com.logub.logcontroller.api.schema import LogubSortDto
from com.logub.logcontroller.domain.model.search import LogubFieldSearch
from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Data
from lombok import NoArgsConstructor


 Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Data @AllArgsConstructor @NoArgsConstructor @Builder(toBuilder = true) public class LogSearchDto
class LogSearchDto:

    def __init__(self):
        
        self.__texts = emptyList()
        self.__systemProperties = emptyList()
        self.__businessProperties = emptyList()
        self.__basicProperties = emptyList()
        self.__limit = 25
        self.__offset = 0
        self.__levels = java.util.Collections.emptyList()
        self.__sort = java.util.Optional.empty()
        self.__beginAt = java.time.Instant.now().minus(15, java.time.temporal.ChronoUnit.MINUTES)
        self.__endAt = java.time.Instant.now()
