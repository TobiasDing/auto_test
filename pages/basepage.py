from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from common.CapPic import cap_pic
from selenium.webdriver.support import expected_conditions as EC
from common.LogGen import Logger

logger = Logger(logger='BasePage').get_log()

class BasePage(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_element(self, *loc):