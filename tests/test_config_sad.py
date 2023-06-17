
import pytest

from src.configs import Configs


@pytest.fixture(scope="function")
def config_file_name():
    return "./tests/assets/config_malfromed_json_syntax.json"

@pytest.mark.skip()
def test_open_missing_config():
    with pytest.raises(Exception) as exp:
        Configs("fake_dir/fake_config.json")

    assert str(exp.value) == "Config file 'fake_dir/fake_config.json' not found."


def test_json_syntax_error(config_file_name):
    with pytest.raises(ValueError) as exp:
        config=Configs(config_file_name)

    assert "Invalid JSON format in config file:" in str(exp.value)
