from com.logub.logcontroller.api.search import LogSearchDto
from com.logub.logcontroller.api import LogubLogDto
from com.logub.logcontroller.api import SystemPropertiesDto
from com.logub.logcontroller.api.schema import BusinessFieldDto
from com.logub.logcontroller.api.schema import LogubSortDto
from com.logub.logcontroller.domain.model.search import LogSearch
from com.logub.logcontroller.domain.model import LogubLog
from com.logub.logcontroller.domain.model import LogubSort
from com.logub.logcontroller.domain.model import SystemProperties
from com.logub.logcontroller.domain.model.schema import BusinessField
from org.mapstruct import Mapper

#ORIGINAL LINE: @Mapper(componentModel = "spring") public abstract class WebMapper
class WebMapper:
    def toDomain(self, log):
        pass
    def toDomain(self, log):
        pass
    def toDomain(self, log):
        pass
    def toDomain(self, value):
        return value.map(self::toDomain)
    def toDomain(self, value):
        pass
    def mapLogubSort(self, value):
        return value.map(self::toDomain)
    def toDomain(self, field):
        pass
    def toWeb(self, log):
        pass
    def toWeb(self, log):
        pass
    def toWeb(self, log):
        pass
    def toWeb(self, value):
        return value.map(self::toWeb)
    def toWeb(self, field):
        pass

    def toWeb(self, value):
        pass
    def toWebLogubSort(self, value):
        return value.map(self::toWeb)
