from com.logub.logcontroller.domain import DomainMapper
from com.logub.logcontroller.domain.model.search import LogSearch
from com.logub.logcontroller.domain.model import LogubLog
from com.logub.logcontroller.repository import LogRepository
from lombok.extern.slf4j import Slf4j
from org.springframework.beans.factory.annotation import Autowired
from org.springframework.stereotype import Service

#ORIGINAL LINE: @Service @Slf4j public class LogService
class LogService:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__logRepository = None
        self.__mapper = None



    def saveLog(self, log):

        self.__logRepository.save(self.__mapper.toRepository(log))

    def searchLog(self, search):
        return self.__logRepository.search(search).stream().map(lambda v : self.__mapper.toDomain(v)).collect(java.util.stream.Collectors.toList())
