
import json

import pytest

from src.configs import Configs


@pytest.fixture
def config_file_name():
    return "./tests/assets/config_malfromed_json_syntax.json"


def test_open_missing_config():
    with pytest.raises(Exception) as exp:
        Configs("fake_dir/fake_config.json")

    assert str(exp.value) == "Config file 'fake_dir/fake_config.json' not found."

