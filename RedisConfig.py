from com.fasterxml.jackson.annotation import JsonInclude
from com.fasterxml.jackson.databind import DeserializationFeature
from com.fasterxml.jackson.databind import ObjectMapper
from com.fasterxml.jackson.datatype.jdk8 import Jdk8Module
from com.fasterxml.jackson.datatype.jsr310 import JavaTimeModule
from com.fasterxml.jackson.module.paramnames import ParameterNamesModule
from org.springframework.beans.factory.annotation import Autowired
from org.springframework.beans.factory.annotation import Value
from org.springframework.context.annotation import Bean
from org.springframework.context.annotation import Configuration
from org.springframework.data.redis.connection import RedisConnectionFactory
from org.springframework.data.redis.connection import RedisStandaloneConfiguration
from org.springframework.data.redis.connection.jedis import JedisConnectionFactory
from org.springframework.data.redis.core import RedisTemplate
from org.springframework.data.redis.hash import Jackson2HashMapper
from org.springframework.data.redis.serializer import GenericJackson2JsonRedisSerializer
from org.springframework.data.redis.serializer import StringRedisSerializer
from redis.clients.jedis import JedisPoolConfig


#ORIGINAL LINE: @Configuration public class RedisConfig
class RedisConfig:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__adresse = None
        self.__port = 0



#ORIGINAL LINE: @Bean public com.fasterxml.jackson.databind.ObjectMapper objectMapper()
    def objectMapper(self):
        objectMapper = com.fasterxml.jackson.databind.ObjectMapper()
        objectMapper.registerModule(com.fasterxml.jackson.datatype.jdk8.Jdk8Module()).registerModule(com.fasterxml.jackson.module.paramnames.ParameterNamesModule()).registerModule(com.fasterxml.jackson.datatype.jsr310.JavaTimeModule())

        objectMapper.setSerializationInclusion(com.fasterxml.jackson.annotation.JsonInclude.Include.NON_NULL)
        #objectMapper.configure(DeserializationFeature.READ_UNKNOWN_ENUM_VALUES_AS_NULL, false)
        objectMapper.configure(com.fasterxml.jackson.databind.DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, False)
        df = java.text.SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSS'Z'")
        objectMapper.setDateFormat(df)
        return objectMapper


#ORIGINAL LINE: @Bean public org.springframework.data.redis.connection.RedisConnectionFactory connectionFactory()
    def connectionFactory(self):
        return org.springframework.data.redis.connection.jedis.JedisConnectionFactory(org.springframework.data.redis.connection.RedisStandaloneConfiguration(self.__adresse, self.__port))


#ORIGINAL LINE: @Bean public org.springframework.data.redis.core.RedisTemplate<?, ?> redisTemplate(org.springframework.data.redis.connection.RedisConnectionFactory redisConnectionFactory)
    def redisTemplate(self, redisConnectionFactory):

        template = org.springframework.data.redis.core.RedisTemplate()
        template.setConnectionFactory(redisConnectionFactory)
        template.setKeySerializer(org.springframework.data.redis.serializer.StringRedisSerializer())
        template.setHashKeySerializer(org.springframework.data.redis.serializer.StringRedisSerializer())
        template.setHashValueSerializer(org.springframework.data.redis.serializer.StringRedisSerializer())
        return template



#ORIGINAL LINE: @Bean public org.springframework.data.redis.hash.Jackson2HashMapper mapper(@Autowired ObjectMapper objectMapper)
    def mapper(self, objectMapper):
        return org.springframework.data.redis.hash.Jackson2HashMapper(objectMapper, True)
