import json


class Configs():
    def __init__(self, config_file):
        with open(config_file) as f:
            self.config = json.load(f)

        self.read_config()

    def read_config(self):
        self.simple_config_text = self.config["simple_config_text"]



