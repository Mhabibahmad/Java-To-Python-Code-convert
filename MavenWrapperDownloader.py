class MavenWrapperDownloader:

    __WRAPPER_VERSION = "0.5.6"
    #    *
    #     * Default URL to download the maven-wrapper.jar from, if no 'downloadUrl' is provided.
    #     
    __DEFAULT_DOWNLOAD_URL = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/" + __WRAPPER_VERSION + "/maven-wrapper-" + __WRAPPER_VERSION + ".jar"

    #    *
    #     * Path to the maven-wrapper.properties file, which might contain a downloadUrl property to
    #     * use instead of the default one.
    #     
    __MAVEN_WRAPPER_PROPERTIES_PATH = ".mvn/wrapper/maven-wrapper.properties"

    #    *
    #     * Path where the maven-wrapper.jar will be saved to.
    #     
    __MAVEN_WRAPPER_JAR_PATH = ".mvn/wrapper/maven-wrapper.jar"

    #    *
    #     * Name of the property which should be used to override the default download url for the wrapper.
    #     
    __PROPERTY_NAME_WRAPPER_URL = "wrapperUrl"

    @staticmethod
    def main(args):
        print("- Downloader started")
        baseDirectory = File(args[0])
        print("- Using base directory: " + baseDirectory.getAbsolutePath())

        # If the maven-wrapper.properties exists, read it and check if it contains a custom
        # wrapperUrl parameter.
        mavenWrapperPropertyFile = File(baseDirectory, MavenWrapperDownloader.__MAVEN_WRAPPER_PROPERTIES_PATH)
        url = MavenWrapperDownloader.__DEFAULT_DOWNLOAD_URL
        if mavenWrapperPropertyFile.exists():
            mavenWrapperPropertyFileInputStream = None
            try:
                mavenWrapperPropertyFileInputStream = FileInputStream(mavenWrapperPropertyFile)
                mavenWrapperProperties = java.util.Properties()
                mavenWrapperProperties.load(mavenWrapperPropertyFileInputStream)
                url = mavenWrapperProperties.getProperty(MavenWrapperDownloader.__PROPERTY_NAME_WRAPPER_URL, url)
            except IOException as e:
                print("- ERROR loading '" + MavenWrapperDownloader.__MAVEN_WRAPPER_PROPERTIES_PATH + "'")
            finally:
                try:
                    if mavenWrapperPropertyFileInputStream is not None:
                        mavenWrapperPropertyFileInputStream.close()
                except IOException as e:
                    # Ignore ...
                    pass
        print("- Downloading from: " + url)

        outputFile = File(baseDirectory.getAbsolutePath(), MavenWrapperDownloader.__MAVEN_WRAPPER_JAR_PATH)
        if not outputFile.getParentFile().exists():
            if not outputFile.getParentFile().mkdirs():
                print("- ERROR creating output directory '" + outputFile.getParentFile().getAbsolutePath() + "'")
        print("- Downloading to: " + outputFile.getAbsolutePath())
        try:
            MavenWrapperDownloader.__downloadFileFromURL(url, outputFile)
            print("Done")
            System.exit(0)
        except Throwable as e:
            print("- Error downloading")
            e.printStackTrace()
            System.exit(1)

    @staticmethod
#JAVA TO PYTHON CONVERTER WARNING: Method 'throws' clauses are not available in Python:
#ORIGINAL LINE: private static void downloadFileFromURL(String urlString, File destination) throws Exception
    def __downloadFileFromURL(urlString, destination):
        if System.getenv("MVNW_USERNAME") is not None and System.getenv("MVNW_PASSWORD") is not None:
            username = System.getenv("MVNW_USERNAME")
            password = System.getenv("MVNW_PASSWORD").toCharArray()
            Authenticator.setDefault(AuthenticatorAnonymousInnerClass(username, password))
        website = URL(urlString)
        rbc = None
        rbc = Channels.newChannel(website.openStream())
        fos = FileOutputStream(destination)
        fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE)
        fos.close()
        rbc.close()

    class AuthenticatorAnonymousInnerClass(Authenticator):

        def __init__(self, username, password):
            self.__username = username
            self.__password = password

        def getPasswordAuthentication(self):
            return PasswordAuthentication(self.__username, self.__password)

# Main function added by Java to Python Converter:

def main():
    MavenWrapperDownloader.main([])

if __name__ == "__main__":
    main()
