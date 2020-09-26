import time
import os
from selenium import webdriver

def cap_pic(driver):

    pt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    picname = os.path.dirname(os.path.abspath('.')) + '/picture/' + pt + '.png'
    driver.get_screenshot_as_file(picname)

