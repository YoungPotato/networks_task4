import configparser


class Parser:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def get_deception(self, config_name):
        self.config.read(config_name)
        return int(self.config.get("settings", "deception"))
