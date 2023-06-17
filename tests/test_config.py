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


def test_read_config(config):
    assert config.simple_config_text ==  "text_one_liner"
