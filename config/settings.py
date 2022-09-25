import yaml


class Setting:
    DB_URL: str
    JWT_KEY: str

    def __init__(self):
        with open('../app.yaml') as file:
            env_dict = yaml.load(file, Loader=yaml.FullLoader)
            DB_USER_NAME = env_dict.datasource.mysql.username
            DB_PASSWORD = env_dict.datasource.mysql.password
            DB_PORT = env_dict.datasource.mysql.port
            DB_HOST = env_dict.datasource.mysql.host
            DB_DATABASE = env_dict.datasource.mysql.database
            self.DB_URL = f"mysql+aiomysql://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

            self.JWT_KEY = env_dict.jwt.keys

            
settings = Setting()