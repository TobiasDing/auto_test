import configparser
import os

def get_browser_info(name):
    cf = configparser.ConfigParser()
    cf_path = os.path.dirname(os.path.abspath(os.path.abspath('.')))+'/config/config.ini'
    cf.read(cf_path)
    browsername = cf.get('browser', name)
    return browsername

