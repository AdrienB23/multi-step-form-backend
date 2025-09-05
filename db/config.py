from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    db_user: str = "419729"
    db_password: str
    db_host: str = "mysql-challenges.alwaysdata.net"
    db_port: int = 3306
    db_name: str = "challenges_multi_step"
    echo: bool = False
    pool_size: int = 10
    max_overflow: int = 5
    pool_pre_ping: bool = True

    @property
    def database_connectionstring(self):
        return f"mariadb+mysqlconnector://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


    class Config:
        env_file = ".env"
