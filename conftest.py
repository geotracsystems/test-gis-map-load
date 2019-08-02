import pytest


def pytest_addoption(parser):
    parser.addoption("--dbname", action="store")
    parser.addoption("--type", action="store")
    parser.addoption("--stage", action="store")


@pytest.fixture(scope="session")
def dbname(request):
    return request.config.getoption("--dbname")


@pytest.fixture(scope="session")
def type(request):
    return request.config.getoption("--type")


@pytest.fixture(scope="session")
def stage(request):
    return request.config.getoption("--stage")
