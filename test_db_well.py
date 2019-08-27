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


def test_sys_well_column_count(database_connection, dbname, type, stage):
    column_count = utils.sql_helper.column_count(database_connection, dbname, type, stage)
    if dbname == 'warehouse':
        assert column_count == 27
    else:
        assert column_count == 25


@pytest.mark.testindexes
@pytest.mark.parametrize("index_name", [
    "well_can_gid_pk",
    "well_can_code_idx",
    "well_can_countymd_idx",
    "well_can_dls_address_idx",
    "well_can_licensee_idx",
    "well_can_name_idx",
    "well_can_nts_address_idx",
    "well_can_operator_idx",
    "well_can_provstate_idx",
    "well_can_status_idx",
    "well_can_surface_loc_idx",
    "well_can_type_idx",
    "well_can_wellid_idx",
    "well_can_sidx",
])
def test_sys_well_index_exist(database_connection, dbname, type, stage, index_name):
    indexnm = utils.sql_helper.index_exists(database_connection, dbname, type, stage, index_name)
    assert index_name == indexnm


@pytest.mark.parametrize("column_name", [
    "wellid", "uwi", "origsourceid", "gid", "sourceid", "lastmodified", "modifiedby",
])
def test_db_well_nonull(database_connection, dbname, type, stage, column_name):
    assert utils.sql_helper.no_nulls(database_connection, dbname, type, stage, column_name)


@pytest.mark.parametrize("column_name", [
    "wellid", "gid"
])
def test_db_well_unique(database_connection, dbname, type, stage, column_name):
    assert utils.sql_helper.uniqueness(database_connection, dbname, type, stage, column_name)


@pytest.mark.parametrize("column_name", [
    "origsourceid", "modifiedby",
])
def test_db_noblank(database_connection, dbname, type, stage, column_name):
    assert utils.sql_helper.no_blanks(database_connection, dbname, type, stage, column_name)


@pytest.mark.parametrize("column_name, value", [
    ("sour", "''"),
    ("field", "''"),
    ("haccuracy", 1),
])
def test_db_well_always_value(database_connection, dbname, type, stage, column_name, value):
    assert utils.sql_helper.always_value(database_connection, dbname, type, stage, column_name, value)


def test_db_uwi_exits_ab_sk(database_connection, dbname, type, stage):
    assert utils.sql_helper.uwi_exits_ab_sk(database_connection, dbname, type, stage)


@pytest.mark.parametrize("column_name, values", [
    ("provstate", "('AB', 'BC', 'MB', 'SK', 'YT')"),
    ("type", "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 98, 99)"),
    ("status", "(1, 2, 3, 4, 5, 98, 99)"),
])
def test_db_well_values_in(database_connection, dbname, type, stage, column_name, values):
    assert utils.sql_helper.valid_data(database_connection, dbname, type, stage, column_name, values)


def test_db_validate_dls_nts(database_connection, dbname, type, stage):
    # assert utils.sql_helper.dls_nts_validator(database_connection, dbname, type, stage)
    pass
