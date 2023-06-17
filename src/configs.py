import json

from box import Box


class Configs():
    def __init__(self, config_file):
        with open(config_file) as f:
            config_data = json.load(f)
        self.config = Box(config_data)