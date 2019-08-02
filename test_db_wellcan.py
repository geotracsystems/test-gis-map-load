import os
import pytest
import utils.connect
import utils.sql_helper


@pytest.fixture(scope="module")
def database_connection(request, dbname):
    cursor = utils.connect.by_database_string(dbname)

    def cursor_teardown():
        cursor.close()
    request.addfinalizer(cursor_teardown)
    return cursor


def test_db_getcounts(database_connection, dbname, type, stage):
    utils.sql_helper.make_counts(database_connection, dbname, type, stage)
    if stage == 'true':
        stagingtable = '_stage'
    elif stage == 'false':
        stagingtable = ''
    assert os.path.exists(f'counts_{dbname}_{type}{stagingtable}.txt') and \
           os.path.exists(f'counts_{dbname}_{type}{stagingtable}.json')
