from lombok import Data


#ORIGINAL LINE: @Data public class QueryBuilder
class QueryBuilder:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__query = None

        self.__query = StringBuilder()

    def append(self, query):

        queryString = '('+str(query.getQuery())+')'
        if self.__query.length() == 0:
            return self.append(queryString)
        return self.append(" ").append(queryString)

    def append(self, query):
        self.__query.append(query)
        return self

    def append(self, query):
        self.__query.append(query)
        return self

    def toRedisQuery(self):
        finalQuery = str(self.__query)
        finalQuery = finalQuery.replace("\\-@", "-@")
        return finalQuery
    def isBlank(self):
        return str(self.__query).isBlank()


    def isEmpty(self):
        return str(self.__query).isEmpty()
