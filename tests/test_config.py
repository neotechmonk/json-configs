import json
import os

import pytest

from src.configs import Configs


@pytest.fixture
def config_file_name():
    return "./src/config.json"

@pytest.fixture
def config(config_file_name):
    yield Configs(config_file_name)

def test_is_config_json(config):
    assert isinstance(config.config,dict)

@pytest.mark.parametrize("attribute, expected_type, expected_value", [
    ("simple_config_text", str, "text_one_liner"),
    ("simple_config_int", int, 1),
    ("simple_config_dec", float, 9.1)
])
def test_config_contents(config, attribute, expected_type, expected_value):
    assert hasattr(config, attribute)
    assert isinstance(getattr(config, attribute), expected_type)
    assert getattr(config, attribute) == expected_value
