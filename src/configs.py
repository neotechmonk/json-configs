import json


class Configs():
    def __init__(self, config_file):
        with open(config_file) as f:
            self.config = json.load(f)

        self.read_config()



    def read_config(self):
        for key, value in self.config.items():
            setattr(self, key, value)


