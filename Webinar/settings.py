from pydantic import BaseSettings

class Settings(BaseSettings):
    server_host: str = '192.168.221.175'
    server_port: int = 8000
    # database_url: str = 'sqlite:///./database.sqlite3'
    
settungs = Settings(
    # _env_file = '.env.txt', # Для подгрузки из файла
    # _env_file_encoding='utf-8',
)