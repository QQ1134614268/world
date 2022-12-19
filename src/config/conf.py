from config.env_default import USERNAME, PASSWORD, HOST, PORT, WORLD_DB

VERSION = "3.0.0"
JPG = ".jpg"
DEFAULT_TIME_STR = '%Y-%m-%d_%H-%M-%S_%f'
DATE_FORMAT = "%Y-%m-%d"
DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{WORLD_DB}?charset=utf8mb4'
