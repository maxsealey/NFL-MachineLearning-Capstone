import os

# base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# data directory
DATA_DIR = os.path.join(BASE_DIR, 'data')
# path to data files
NFL_DATA_PATH = os.path.join(DATA_DIR, 'nfl_data.csv')
NFL_SQLDB_PATH = os.path.join(DATA_DIR, 'nfl_data.db')


class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = True
