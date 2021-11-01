class BaseConfig:
    DEBUG = True


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    DEBUG = False
