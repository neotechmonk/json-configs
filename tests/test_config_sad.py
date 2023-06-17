
import pytest

from src.configs import Configs


@pytest.fixture
def config_file_name():
    return "./tests/assets/config_malfromed_json_syntax.json"

def test_open_malformed_config(config_file_name):
    with pytest.raises(ValueError) as exp:
        Configs(config_file_name)
    
    assert str(exp.value) == "Invalid input: invalid literal for int() with base 10: ''"
         