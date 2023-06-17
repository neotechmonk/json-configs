import json
import os

import pytest

from src.configs import Configs


@pytest.fixture
def config_file_name():
    return "./src/config.json"

@pytest.fixture
def config(config_file_name):
    yield Configs(config_file_name).config

def test_is_config_json(config):
    assert isinstance(config,dict)

@pytest.mark.parametrize("attribute, expected_type, expected_value", [
    ("simple_config_text", str, "text_one_liner"),
    ("simple_config_int", int, 1),
    ("simple_config_dec", float, 9.1)
])
def test_config_contents(config, attribute, expected_type, expected_value):
    assert attribute in config
    assert isinstance(config[attribute], expected_type)
    assert config[attribute] == expected_value

@pytest.mark.parametrize("key, expected_value, expected_type", [
    ("nested_config.nested_level_1", "level 1", str),
    ("nested_config.nested_level_2.nested_level_2_num", 2, int),
    ("nested_config.nested_level_2.nested_level_2_dec",  2.2, float)
])
def test_nested_contents(config, key, expected_value, expected_type):
    keys = key.split(".")
    attribute = config
    for k in keys:
        assert k in attribute
        attribute = attribute[k]
    assert attribute == expected_value
    assert isinstance(attribute, expected_type)
