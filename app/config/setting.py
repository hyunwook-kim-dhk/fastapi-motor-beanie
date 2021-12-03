from pydantic import BaseSettings


class Setting(BaseSettings):
    """
    This class read the environment variables and setup the value
    ex) LOG_LEVEL => log_level
    """

    LOG_LEVEL: str = "INFO"
    MONGODB_URL: str = "mongodb://username:password@localhost:27017/app"
    MONGODB_DBNAME: str = "app"


SETTING = Setting()
