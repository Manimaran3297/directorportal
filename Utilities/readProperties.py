import configparser

Config=configparser.RawConfigParser()
Config.read("/home/ticvictech/PycharmProjects/Directorportal/Configurations/config")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = Config.get('common info','baseURL')
        return url

    @staticmethod
    def getUserName():
        username = Config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password = Config.get('common info','password')
        return password
