from com.logub.logcontroller.domain.model.schema import BusinessField
from com.logub.logcontroller.repository import LogSchemaRepository
from lombok.extern.slf4j import Slf4j
from org.springframework.beans.factory.annotation import Autowired
from org.springframework.stereotype import Service

#ORIGINAL LINE: @Service @Slf4j public class LogSchemaService
class LogSchemaService:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__logSchemaRepository = None


    def getSchema(self):
        return self.__logSchemaRepository.getSchema()

    def indexField(self, field):
        fieldName = "businessProperties." + field.getName()
        self.__logSchemaRepository.indexField(fieldName, field.getType().toRedisSearchType())
