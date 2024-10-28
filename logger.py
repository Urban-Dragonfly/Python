import logging
import os
import sys


# Get the script name that is importing this module
script_name = os.path.basename(sys.argv[0])
script_name_without_extension = os.path.splitext(script_name)[0]
log_file_name = f'logs/{script_name_without_extension}.log'

# Ensure the logs directory exists
os.makedirs('logs', exist_ok=True)

# Configure the logger to log to the constructed log file
logging.basicConfig(filename=log_file_name, encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)