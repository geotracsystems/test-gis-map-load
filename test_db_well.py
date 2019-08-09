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
    "geom", "countymd", "gid", "surface_loc", "field", "deltaflag",
])
def test_db_well_column_exist(database_connection, dbname, type, stage, column_name):
    tablenm, columnnm = utils.sql_helper.column_exists(database_connection, dbname, type, stage, column_name)

    assert tablenm == f"{type}_can{utils.sql_helper.get_stagestr(stage)}" and columnnm == column_name


def test_sys_well_index_exist():
    pass


@pytest.mark.parametrize("column_name", [
    "wellid", "uwi", "origsourceid", "gid"
])
def test_db_well_nonull(database_connection, dbname, type, stage, column_name):
    assert utils.sql_helper.no_nulls(database_connection, dbname, type, stage, column_name)


@pytest.mark.parametrize("column_name", [
    "wellid", "gid"
])
def test_db_well_unique(database_connection, dbname, type, stage, column_name):
    assert utils.sql_helper.uniqueness(database_connection, dbname, type, stage, column_name)


@pytest.mark.parametrize("column_name", [
    "origsourceid",
])
def test_db_noblank(database_connection, dbname, type, stage, column_name):
    assert utils.sql_helper.no_blanks(database_connection, dbname, type, stage, column_name)


@pytest.mark.parametrize("column_name, value", [
    ("sour", "''"),
    ("field", "''"),
    ("haccuracy", 1),
    ("deltaflag", "'I'")
])
def test_db_well_always_value(database_connection, dbname, type, stage, column_name, value):
    assert utils.sql_helper.always_value(database_connection, dbname, type, stage, column_name, value)


def test_db_uwi_exits_ab_sk(database_connection, dbname, type, stage):
    assert utils.sql_helper.uwi_exits_ab_sk(database_connection, dbname, type, stage)


def test_db_validate_dls_nts(database_connection, dbname, type, stage):
    # assert utils.sql_helper.dls_nts_validator(database_connection, dbname, type, stage)
    pass
