from pydantic_settings import BaseSettings 

class Setting(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str 
    MYSQL_DB: str 
    MYSQL_PORT: int 
    MYSQL_HOST: str 

setting = Setting()
