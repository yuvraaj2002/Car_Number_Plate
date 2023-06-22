import logging
from datetime import datetime
import os

# Name of log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Path where logs will be stored
logs_path = os.path.join(os.getcwd(), "Logs", LOG_FILE)
os.makedirs(logs_path,exist_ok= True)

# Path of log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Basic configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("logs directory created")