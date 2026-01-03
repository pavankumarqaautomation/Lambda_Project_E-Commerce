import logging
import os
from datetime import datetime


class LogGen:
    @staticmethod
    def loggen():
        log_dir = os.path.join(os.getcwd(), "logs")
         # 🔑 CREATE logs folder if not exists (Jenkins fix)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir,f"automation_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log")
        
        #path = os.path.abspath(os.curdir + f"/logs/automation_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log")
        logging.basicConfig(filename=log_file,
                            format='%(asctime)s : %(levelname)s : %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

