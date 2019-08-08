import os
import pytest
import utils.connect
import utils.sql_helper
import utils.count_helper


@pytest.fixture(scope="module")
def database_connection(request, dbname):
    cursor = utils.connect.by_database_string(dbname)

    def cursor_teardown():
        cursor.close()
    request.addfinalizer(cursor_teardown)
    return cursor


def test_db_getcounts(database_connection, dbname, type, stage):
    utils.count_helper.make_counts(database_connection, dbname, type, stage)

    assert os.path.exists(f'counts_{dbname}_{type}_can{utils.sql_helper.get_stagestr(stage)}.txt') and \
           os.path.exists(f'counts_{dbname}_{type}_can{utils.sql_helper.get_stagestr(stage)}.json')


@pytest.mark.parametrize("column_name", [
    "wellid", "uwi", "origsourceid", "type", "status", "sour", "name", "licensee", "operator", "spuddate", "licdate",
    "haccuracy", "dls_address", "nts_address", "provstate", "sourceid", "lastmodified", "modifiedby", "remarks",
    "geom", "countymd", "gid", "surface_loc", "field", "deltaflag", "gojo"
])
def test_db_well_column_exist(database_connection, dbname, type, stage, column_name):
    tablenm, columnnm = utils.sql_helper.column_exists(database_connection, dbname, type, stage, column_name)

    assert tablenm == f"{type}_can{utils.sql_helper.get_stagestr(stage)}" and columnnm == column_name


def test_db_unique_id(database_connection, dbname, type, stage):
    id = f"{type}id"
    assert utils.sql_helper.uniqueness(database_connection, dbname, type, stage, id)


def test_db_nonull_id(database_connection, dbname, type, stage):
    id = f"{type}id"
    assert utils.sql_helper.no_nulls(database_connection, dbname, type, stage, id)


def test_db_nonull_origsourceid(database_connection, dbname, type, stage):
    assert utils.sql_helper.no_nulls(database_connection, dbname, type, stage, 'origsourceid')


def test_db_noblank_origsourceid(database_connection, dbname, type, stage):
    assert utils.sql_helper.no_blanks(database_connection, dbname, type, stage, 'origsourceid')
