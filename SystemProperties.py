
#import static lombok.AccessLevel.PRIVATE

from lombok import AllArgsConstructor
from lombok import Builder
from lombok import Value

#ORIGINAL LINE: @Value @AllArgsConstructor(access = PRIVATE) @Builder(toBuilder = true) public class SystemProperties
class SystemProperties:

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self.imageName = java.util.Optional.empty()
        self.containerName = java.util.Optional.empty()
        self.containerId = java.util.Optional.empty()
        self.env = java.util.Optional.empty()
        self.host = java.util.Optional.empty()
