import pytest
import utils.connect


@pytest.fixture(scope="module")
def database_connection(dbname):
    cursor = utils.connect('PostgreSQL Unicode')