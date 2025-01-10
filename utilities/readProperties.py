import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + '\\configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('Paths', 'baseURL')
        return url

    @staticmethod
    def getFirefoxdriver():
        geckodriver = config.get('Paths', 'geckodriver_path')
        return geckodriver

    @staticmethod
    def getFirefoxPath():
        firefox_path = config.get('Paths', 'firefox_path')
        return firefox_path

    @staticmethod
    def getCSV_Path():
        csvFile_path = config.get('Paths', 'csv_file')
        return csvFile_path

    @staticmethod
    def getchromedriver():
        chromedriver = config.get('Paths', 'chromedriver')
        return chromedriver

    @staticmethod
    def getChromePath():
        chrome_path = config.get('Paths', 'chrome_path')
        return chrome_path
