from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Data
from lombok import NoArgsConstructor


#ORIGINAL LINE: @Data @AllArgsConstructor @NoArgsConstructor @Builder(toBuilder = true) public class RSystemProperties implements java.io.Serializable
class RSystemProperties:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.__imageName = None
        self.__containerName = None
        self.__env = None
        self.__host = None
        self.__containerId = None
