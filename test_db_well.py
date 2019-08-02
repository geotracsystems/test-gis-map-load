import pytest
import utils.connect


@pytest.fixture(scope="module")
def database_connection(request, dbname):
    cursor = utils.connect.by_database_string(dbname)

    def cursor_teardown():
        cursor.close()

    request.addfinalizer(cursor_teardown)
    return cursor


def test_db_getcounts(database_connection, type, stage: bool):
    pass




