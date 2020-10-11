import os

from myservice.config import ProdConfig, DevConfig


class Util:
    config = None

    @classmethod
    def init_config(cls):
        env = os.getenv('ENVIRONMENT').lower()
        if env == 'dev':
            cls.config = DevConfig
        elif env == 'prod':
            cls.config = ProdConfig

    @classmethod
    def get_app_config(cls):
        return cls.config
