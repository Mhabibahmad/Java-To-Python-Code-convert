from com.logub.logcontroller.api.search import LogSearchDto
from com.logub.logcontroller.api import LogubLogDto
from com.logub.logcontroller.domain.service import LogService
from org.springframework.beans.factory.annotation import Autowired
from org.springframework.web.bind.annotation import CrossOrigin
from org.springframework.web.bind.annotation import PostMapping
from org.springframework.web.bind.annotation import RequestBody
from org.springframework.web.bind.annotation import RequestMapping
from org.springframework.web.bind.annotation import RestController


#ORIGINAL LINE: @RestController @RequestMapping("/logs") @CrossOrigin(origins = "*") public class LogController
class LogController:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__logService = None
        self.__mapper = None



#ORIGINAL LINE: @PostMapping public void logs(@RequestBody LogubLogDto logDto)
    def logs(self, logDto):
        self.__logService.saveLog(self.__mapper.toDomain(logDto))

#ORIGINAL LINE: @PostMapping(path = "/search") public java.util.List<com.logub.logcontroller.api.LogubLogDto> searchLog(@RequestBody LogSearchDto logDto)
    def searchLog(self, logDto):
        return self.__logService.searchLog(self.__mapper.toDomain(logDto)).stream().map(lambda v : self.__mapper.toWeb(v)).collect(java.util.stream.Collectors.toList())

from com.logub.logcontroller.api.search import LogSearchDto
from com.logub.logcontroller.api import LogubLogDto
from com.logub.logcontroller.domain.service import LogService
from org.springframework.beans.factory.annotation import Autowired
from org.springframework.web.bind.annotation import CrossOrigin
from org.springframework.web.bind.annotation import PostMapping
from org.springframework.web.bind.annotation import RequestBody
from org.springframework.web.bind.annotation import RequestMapping
from org.springframework.web.bind.annotation import RestController


#ORIGINAL LINE: @RestController @RequestMapping("/logs") @CrossOrigin(origins = "*") public class LogController
    class LogController:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.__logService = None
            self.__mapper = None




#ORIGINAL LINE: @PostMapping public void logs(@RequestBody LogubLogDto logDto)
        def logs(self, logDto):
            self.__logService.saveLog(self.__mapper.toDomain(logDto))

#ORIGINAL LINE: @PostMapping(path = "/search") public java.util.List<com.logub.logcontroller.api.LogubLogDto> searchLog(@RequestBody LogSearchDto logDto)
        def searchLog(self, logDto):
            return self.__logService.searchLog(self.__mapper.toDomain(logDto)).stream().map(lambda v : self.__mapper.toWeb(v)).collect(java.util.stream.Collectors.toList())
