import json

from box import Box


class Configs():
    def __init__(self, config_file):
        try:
            with open(config_file) as f:
                config_data = json.load(f)
                
            self.config = Box(config_data)
        except FileNotFoundError:
            print(f"Error: Config file '{config_file}' not found.")
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format in config file. {str(e)}")
