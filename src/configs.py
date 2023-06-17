import json

from box import Box


class Configs():
    def __init__(self, config_file):
        try:
            with open(config_file) as f:
                config_data = json.load(f)
            self.config = Box(config_data)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file '{config_file}' not found.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in config file: {str(e)}")
        except Exception as e: 
             raise Exception(f"Unknown Error in loading config file: {str(e)}")