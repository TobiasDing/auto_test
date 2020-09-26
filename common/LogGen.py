import logging
import os
import time

class Logger(object):
    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        lt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        log_name = os.path.dirname(os.path.abspath('.'))+f'/log/{lt}.log'
        fileh = logging.FileHandler(log_name)
        fileh.setLevel(logging.INFO)

        consoleh = logging.StreamHandler()
        consoleh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileh.setFormatter(formatter)
        consoleh.setFormatter(formatter)
        self.logger.addHandler(consoleh)
        self.logger.addHandler(fileh)

    def get_log(self):
        return self.logger