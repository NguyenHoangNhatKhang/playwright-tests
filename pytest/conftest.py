import pytest
@pytest.fixture(scope="function")
def preSetupWork():
    print("i set up browser instance")