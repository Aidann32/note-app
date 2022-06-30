from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists

import logging
import os

from config import LOGS_DIRECTORY, DB_FILE_DIRECTORY

log_file = os.path.join(LOGS_DIRECTORY, 'db_starter.log')
logging.basicConfig(filename=log_file, filemode='w+', level=logging.DEBUG, format='%(asctime)s - %(message)s')
logger = logging.getLogger('db_starter')

def create_tables(engine, *args):
    for meta in args:
        meta.create_all(engine)

class DBStarter:
    def __init__(self, db_name: str, db_engine: str):
        self.db_name = db_name
        self.db_engine = db_engine
        self.db_absolute_path = os.path.join(DB_FILE_DIRECTORY, f'{self.db_name}.db')

    def create_database(self) -> bool:
        if self.db_engine == 'sqlite':
            try:
                if not database_exists(f'sqlite:///{self.db_absolute_path}'):
                    from tables.note import meta
                    engine = create_engine(f'sqlite:///{self.db_absolute_path}', echo = True)
                    create_tables(engine, meta)
                    logger.info(f'Database {self.db_name} succesfully created')
                    return True

            except Exception as e:
                logger.critical(f'Database creation error: {str(e)}')
                return False

            