from com.google.common.collect import Streams

from com.fasterxml.jackson.databind import ObjectMapper
from com.logub.logcontroller.domain.model import LogubSort
from com.logub.logcontroller.domain.model.search import LogSearch
from com.logub.logcontroller.domain.query.redis.search import QueryBuilder
from com.logub.logcontroller.domain.query.redis.search import QueryBuilders
from com.logub.logcontroller.repository.model import RLogubLog
from io.redisearch import Document
from io.redisearch import Query
from io.redisearch.client import Client
from lombok.extern.slf4j import Slf4j
from org.springframework.beans.factory.annotation import Autowired
from org.springframework.beans.factory.annotation import Value
from org.springframework.data.redis.hash import Jackson2HashMapper
from org.springframework.stereotype import Repository


#ORIGINAL LINE: @Repository @Slf4j public class LogRepository
class LogRepository:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__INDEX_NAME = "log"
        self.__adresse = None
        self.__port = 0
        self.__jackson2HashMapper = None
        self.__objectMapper = None
        self.__redisSearchClient = None




    def save(self, log):

        self.__redisSearchClient.addDocument("log:" + log.getId(), self.__jackson2HashMapper.toHash(log))

    #  *
    #   * Search list.
    #   *
    #   * @param logSearch the log search
    #   * @return the list
    #   
    def search(self, logSearch):
        queryString = logSearch.toQuery()
        query = None
        if queryString.isBlank():
            query = (io.redisearch.Query("*")).limit(logSearch.getOffset(), logSearch.getLimit())
        else:
            query = (io.redisearch.Query(queryString.toRedisQuery())).limit(logSearch.getOffset(), logSearch.getLimit())
        if logSearch.getSort().isPresent():
            query.setSortBy(logSearch.getSort().get().getField(), logSearch.getSort().get().getOrder() is com.logub.logcontroller.domain.model.LogubSort.LogubOrder.ASC)
        else:
            query.setSortBy("timestamp", False)
        query.addFilter(com.logub.logcontroller.domain.query.redis.search.QueryBuilders.filterNumeric("timestamp", logSearch.getBeginAt(), logSearch.getEndAt()))
        docs = self.__redisSearchClient.search(query).docs
        return docs.stream().map(lambda v : com.google.common.collect.Streams.stream(v.getProperties()).collect(java.util.stream.Collectors.toMap(java.util.Map.Entry::getKey, java.util.Map.Entry::getValue))).map(lambda v : self.__objectMapper.convertValue(self.__jackson2HashMapper.fromHash(v), com.logub.logcontroller.repository.model.RLogubLog.class)).collect(java.util.stream.Collectors.toList())

#ORIGINAL LINE: @PostConstruct public void createConnector()
    def createConnector(self):

        try:
            self.__redisSearchClient = io.redisearch.client.Client(self.__INDEX_NAME, self.__adresse, self.__port)
        except Exception as exception:
            log.warn("createConnector", exception)
