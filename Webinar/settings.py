from pydantic import BaseSettings

class Settings(BaseSettings):
    server_host: str = '192.168.221.175'
    server_port: int = 8000 
    token = "gsdfgadfh3123jiasd412" # Хз где токен хранить
    server_frequency_rate = 1
    # database_url: str = 'sqlite:///./database.sqlite3'

settungs = Settings()