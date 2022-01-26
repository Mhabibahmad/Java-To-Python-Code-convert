from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Data
from lombok import NoArgsConstructor


#ORIGINAL LINE: @Data @AllArgsConstructor @NoArgsConstructor @Builder(toBuilder = true) public class SystemPropertiesDto
class SystemPropertiesDto:

    def __init__(self):
        self.__imageName = java.util.Optional.empty()
        self.__containerName = java.util.Optional.empty()
        self.__env = java.util.Optional.empty()
        self.__host = java.util.Optional.empty()
        self.containerId = java.util.Optional.empty()
