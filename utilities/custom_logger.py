# importing module
import logging


class Log_Maker:
   @staticmethod
   def log_gen():
       # Create and configure logger
       logging.basicConfig(filename=".\\logs\\nopcommerce.log",
                   format='%(asctime)s : %(levelname)s :%(message)s',
                   filemode='w', force=True)


       # Creating an object
       logger = logging.getLogger()


       # Setting the threshold of logger to DEBUG
       logger.setLevel(logging.INFO)


       return logger