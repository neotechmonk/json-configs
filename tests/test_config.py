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

def test_config_contents(config):
    assert all([
        isinstance(config.simple_config_text, str),
        config.simple_config_text == "text_one_liner"
    ])

    
