from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    server_host: str = '192.168.221.175'
    server_port: int = 8000 
    token = "gsdfgadfh3123jiasd412" # Хз где токен хранить
    path_to_downloads = os.path.dirname(os.path.realpath(__file__)) + "\downloads"
    # database_url: str = 'sqlite:///./database.sqlite3'

settungs = Settings()