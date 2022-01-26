from com.logub.logcontroller.api.schema import BusinessFieldDto
from com.logub.logcontroller.domain.service import LogSchemaService
from org.springframework.beans.factory.annotation import Autowired
from org.springframework.web.bind.annotation import CrossOrigin
from org.springframework.web.bind.annotation import GetMapping
from org.springframework.web.bind.annotation import PostMapping
from org.springframework.web.bind.annotation import RequestBody
from org.springframework.web.bind.annotation import RequestMapping
from org.springframework.web.bind.annotation import RestController

#ORIGINAL LINE: @RestController @RequestMapping("/logs/schema") @CrossOrigin(origins = "*") public class LogSchemaController
class LogSchemaController:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__logService = None
        self.__mapper = None


    #  *
    #   * Search log list.
    #   *
    #   * @return the list
    #   
#ORIGINAL LINE: @GetMapping public java.util.List<String> getSchema()
    def getSchema(self):
        return self.__logService.getSchema()

#ORIGINAL LINE: @PostMapping public void addField(@RequestBody BusinessFieldDto field)
    def addField(self, field):
        self.__logService.indexField(self.__mapper.toDomain(field))

from com.logub.logcontroller.api.schema import BusinessFieldDto
from com.logub.logcontroller.domain.service import LogSchemaService
from org.springframework.beans.factory.annotation import Autowired
from org.springframework.web.bind.annotation import CrossOrigin
from org.springframework.web.bind.annotation import GetMapping
from org.springframework.web.bind.annotation import PostMapping
from org.springframework.web.bind.annotation import RequestBody
from org.springframework.web.bind.annotation import RequestMapping
from org.springframework.web.bind.annotation import RestController

#ORIGINAL LINE: @RestController @RequestMapping("/logs/schema") @CrossOrigin(origins = "*") public class LogSchemaController
    class LogSchemaController:

        def __init__(self):
            #instance fields found by Java to Python Converter:
            self.__logService = None
            self.__mapper = None



        #  *
        #   * Search log list.
        #   *
        #   * @return the list
        #   
#ORIGINAL LINE: @GetMapping public java.util.List<String> getSchema()
        def getSchema(self):
            return self.__logService.getSchema()
#ORIGINAL LINE: @PostMapping public void addField(@RequestBody BusinessFieldDto field)
        def addField(self, field):
            self.__logService.indexField(self.__mapper.toDomain(field))
