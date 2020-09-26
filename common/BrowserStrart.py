from common.ReadConfig import get_browser_info
from selenium import webdriver
import os
from common.CapPic import cap_pic
from common.LogGen import Logger

logger = Logger(logger='浏览器启动加载').get_log()


def browser_start():
    browser_name = get_browser_info('BrowserName')
    url = get_browser_info('Url')
    if browser_name == 'Chrome':
        logger.info('启动Chrome浏览器')
        driver = webdriver.Chrome()
        logger.info(f'访问{url}')
        driver.get(url)
    return driver


if __name__ == '__main__':
    driver = browser_start()
    cap_pic(driver)
