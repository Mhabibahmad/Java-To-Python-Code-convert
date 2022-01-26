from com.logub.logcontroller.domain.model import LogLevel
from com.logub.logcontroller.repository.model import RLogubLog
from com.logub.logcontroller.repository.model import RSystemProperties
from io.redisearch import Schema
from io.redisearch.client import Client
from lombok.extern.slf4j import Slf4j
from org.springframework.beans.factory.annotation import Autowired
from org.springframework.beans.factory.annotation import Value
from org.springframework.data.redis.core import RedisTemplate
from org.springframework.data.redis.hash import Jackson2HashMapper
from org.springframework.stereotype import Repository


#ORIGINAL LINE: @Repository @Slf4j public class LogSchemaRepository
class LogSchemaRepository:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__INDEX_SCHEMA = "schema"
        self.__INDEX_LOG = "log"
        self.__adresse = None
        self.__port = 0
        self.__jackson2HashMapper = None
        self.__redisTemplate = None
        self.__redisSearchClient = None



    def getSchema(self):
        return self.__redisTemplate.opsForList().range(self.__INDEX_SCHEMA + ":1", 0, -1)

#ORIGINAL LINE: @PostConstruct public void initSchema()
    def initSchema(self):
        h = self.__INDEX_SCHEMA + ":1"
        schemeSet = self.getSchema() if self.__redisTemplate.hasKey(h) else java.util.Collections.emptyList()
        fields = self.__jackson2HashMapper.toHash(com.logub.logcontroller.repository.model.RLogubLog.builder().level(com.logub.logcontroller.domain.model.LogLevel.ERROR).message("nothing").timestamp(java.time.Instant.now().toEpochMilli()).systemProperties(com.logub.logcontroller.repository.model.RSystemProperties.builder().containerName("nothing").env("env").host("host").imageName("imagename").containerName("unknow").containerId("ZZZ").build()).thread("1").service("app").logger("logger").source("stdout").build())
        systemField = fields.keys()
        schemeSet.forEach(systemField::remove)
        log.info("new fields : {}", systemField)
        if not systemField.isEmpty():
            self.__redisTemplate.opsForList().rightPushAll(h, list(systemField))
        try:
            self.__redisSearchClient = io.redisearch.client.Client(self.__INDEX_LOG, self.__adresse, self.__port)
            schema = self.__createSchema()
            self.__redisSearchClient.createIndex(schema, io.redisearch.client.Client.IndexOptions.defaultOptions())
        except Exception as exception:
            log.warn("createClientAndSchema", exception)
            info = (self.__redisSearchClient.getInfo().get("fields")).stream().filter(lambda v : (not v.isEmpty())).map(lambda v : str(v.get(0))).collect(java.util.stream.Collectors.toList())
            for field in self.getSchema():
                if info.stream().anyMatch(lambda v : v is field):
                    log.info("value already present in schema {}", field)
                    continue
                if field == "message":
                    self.__redisSearchClient.alterIndex(io.redisearch.Schema.Field(field, io.redisearch.Schema.FieldType.FullText, True))
                else:
                    log.info("new global properties detected {}", field)
                    self.__redisSearchClient.alterIndex(io.redisearch.Schema.Field(field, io.redisearch.Schema.FieldType.Tag, True))

    def indexField(self, fieldName, fieldType):
        self.__redisSearchClient.alterIndex(io.redisearch.Schema.Field(fieldName, fieldType, True))
        self.__redisTemplate.opsForList().rightPush(self.__INDEX_SCHEMA + ":1", fieldName)



    def __createSchema(self):
        schema = io.redisearch.Schema()
        for field in self.getSchema():
            if field == "message":
                schema.addField(io.redisearch.Schema.Field(field, io.redisearch.Schema.FieldType.FullText, True))
            elif field == "timestamp":
                schema.addField(io.redisearch.Schema.Field(field, io.redisearch.Schema.FieldType.Numeric, True))
            else:
                schema.addField(io.redisearch.Schema.Field(field, io.redisearch.Schema.FieldType.Tag, True))
        return schema
