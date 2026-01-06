import inspect
import logging


class Utils:
    def findlistitems(self, list, value):

        for item in list:
            print("the number of item is" + item.text)
            assert item.text == value
            print("assert pass")

    def custom_logger(self, logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        fh = logging.FileHandler("automation.log")

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger