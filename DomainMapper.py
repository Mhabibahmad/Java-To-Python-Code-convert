from com.logub.logcontroller.domain.model import LogubLog
from com.logub.logcontroller.domain.model import LogubSchema
from com.logub.logcontroller.repository.model import RLogubLog
from com.logub.logcontroller.repository.model.schema import RLogubSchema
from org.mapstruct import Mapper


#ORIGINAL LINE: @Mapper(componentModel = "spring") public abstract class DomainMapper
class DomainMapper:
    def toRepository(self, log):
        pass
    def toRepository(self, log):
        pass
    def toDomain(self, log):
        pass
    def toDomain(self, log):
        pass
    def map(self, string):
        return string.orElse(None)
    def map(self, now):
        return now.toEpochMilli()

    def map(self, now):
        return java.time.Instant.ofEpochMilli(now)

    def map(self, string):
        return java.util.Optional.ofNullable(string)
