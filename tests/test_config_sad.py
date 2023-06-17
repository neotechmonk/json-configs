
import pytest

from src.configs import Configs


@pytest.fixture(scope="function")
def config_file_syntax_error():
    return "./tests/assets/config_malfromed_json_syntax.json"

@pytest.fixture(scope="function")
def config_file_missing():
    return "./fake_dir/fake_config.json"


@pytest.mark.skip()
def test_open_missing_config(config_file_missing):
    with pytest.raises(Exception) as exp:
        Configs(config_file_missing)

    assert str(exp.value) == "Config file 'fake_dir/fake_config.json' not found."


def test_json_syntax_error(config_file_syntax_error):
    with pytest.raises(ValueError) as exp:
        config=Configs(config_file_syntax_error)

    assert "Invalid JSON format in config file:" in str(exp.value)
