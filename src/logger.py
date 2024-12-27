# -*- coding: utf-8 -*-
"""logger.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1euT2h8iPOtELBRJ-6vMOEZ9sArllmnbQ
"""



import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok = True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level  = logging.INFO,
)












