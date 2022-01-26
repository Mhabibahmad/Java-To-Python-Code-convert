from io.redisearch import Query


class QueryBuilders:

    @staticmethod
    def tag(field, value, negative):
        return com.logub.logcontroller.domain.query.redis.search.QueryBuilders.tag(field, java.util.Collections.singletonList(value), negative)

    @staticmethod
    def tag(field, negative, *values):
        return com.logub.logcontroller.domain.query.redis.search.QueryBuilders.tag(field, java.util.Arrays.asList(values), negative)

    @staticmethod
    def tag(field, values, negative):
        queryBuilder = (QueryBuilder()).append(com.logub.logcontroller.domain.query.redis.search.QueryBuilders.__fieldToRedisField(com.logub.logcontroller.domain.query.redis.search.QueryBuilders.cleanString(field), negative)).append(":{")
        i = 0
        while i < len(values):
            queryBuilder.append(com.logub.logcontroller.domain.query.redis.search.QueryBuilders.cleanString(values[i]))
            if i != len(values) - 1:
                queryBuilder.append('|')
            i += 1
        queryBuilder.append('}')
        return queryBuilder

    @staticmethod
    def text(field, text, negative):
        queryBuilder = (QueryBuilder()).append(com.logub.logcontroller.domain.query.redis.search.QueryBuilders.__fieldToRedisField(com.logub.logcontroller.domain.query.redis.search.QueryBuilders.cleanString(field), negative)).append(':')
        text = text.trim()
        if text.startswith("*"):
            text = text[1:]
        if not text.isBlank():
            queryBuilder.append(com.logub.logcontroller.domain.query.redis.search.QueryBuilders.cleanString(text))
        return queryBuilder

    @staticmethod
    def filterNumeric(field, beginAt, endAt):
        return io.redisearch.Query.NumericFilter(field, beginAt.toEpochMilli(), endAt.toEpochMilli())

    @staticmethod
    def __fieldToRedisField(field, negative):
        field = '@' + field
        if negative:
            field = '-' + field
        return field
    @staticmethod
    def cleanString(value):
        for c in "\\,/.<>{}[]\"':;!@#$%^&()-+=~".toCharArray():
            value = value.replace(""+c, "\\"+c)
        return value
