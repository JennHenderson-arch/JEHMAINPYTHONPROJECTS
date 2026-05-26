# A set of functions and fixtures for pytest that can be used across multiple test files. This includes a fixture to check if the tests are running in a CI environment and a fixture to pause execution for debugging purposes when not in CI.

import os
import time
import pytest

@pytest.fixture(scope="session")
def is_ci():
    return os.getenv("CI") == "true"

@pytest.fixture
def debug_pause(is_ci):
    def pause(seconds):
        if not is_ci:
            time.sleep(seconds)
    return pause

""" @pytest.fixture
def debug_print(is_ci):
    def log(msg):
        if not is_ci:
            print(msg)
    return log """
