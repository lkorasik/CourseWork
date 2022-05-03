from configparser import ConfigParser


class Config:
    def __init__(self):
        config = ConfigParser()
        config.read('config.properties')

        self.core_count = config["DEFAULT"]["core.count"]
