import os

dir_path = os.path.dirname(os.path.realpath(__file__))

LOGS_DIRECTORY = os.path.join(dir_path, 'logs')
DB_FILE_DIRECTORY = dir_path