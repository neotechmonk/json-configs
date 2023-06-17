from configs import Configs

if __name__ == '__main__':
    config = Configs("./src/config.json")
    print (config.simple_config_text)