import eel

import logging
import os

from db import DBStarter
from config import LOGS_DIRECTORY, DB_FILE_DIRECTORY

log_file = os.path.join(LOGS_DIRECTORY, 'main.log')
logging.basicConfig(filename=log_file, filemode='w+', level=logging.DEBUG, format='%(asctime)s - %(message)s')
logger = logging.getLogger('main')

try:
    eel.init('webinterface', allowed_extensions=['.js', '.html'])

    db_starter = DBStarter('notes', 'sqlite')
    db_starter.create_database()

    eel.start('templates/base.html', port=8001, jinja_templates='templates', geometry={'position': (0,0)})
    logger.info('Start of app is successfull')
    
except Exception as e:
    logger.critical(f'App stopped working. Exception message:{str(e)}')
