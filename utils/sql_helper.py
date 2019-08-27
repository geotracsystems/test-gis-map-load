def get_stagestr(stage):
    if stage == 'true':
        stagingtable = '_stage'
    elif stage == 'false':
        stagingtable = ''
    return stagingtable


def get_count(cursor, sqlquery):
    cursor.execute(sqlquery)
    row = cursor.fetchone()
    if row:
        return row[0]


def column_exists(cursor, dbname, type, stage, column):
    column_exist_sql = (
        f"SELECT table_name, column_name FROM information_schema.columns WHERE "
        f"table_name = '{type}_can{get_stagestr(stage)}' AND  "
        f"column_name = '{column}'"
    )
    cursor.execute(column_exist_sql)

    row = cursor.fetchone()
    table_name, column_name = row[0], row[1]
    return table_name, column_name


def column_count(cursor, dbname, type, stage):
    column_count_sql = (
        f"SELECT COUNT(column_name) FROM information_schema.columns WHERE "
        f"table_name = '{type}_can{get_stagestr(stage)}'"
    )

    return get_count(cursor, column_count_sql)


def index_exists(cursor, dbname, type, stage, index):
    index_exist_sql = (
        f"SELECT name from sys.indexes where "
        f"object_id = OBJECT_ID('dbo.{type}_can{get_stagestr(stage)}')"
        f"AND name = '{index}'"
    )
    cursor.execute(index_exist_sql)
    row = cursor.fetchone()
    index_name = row[0]
    return index_name


def uniqueness(cursor, dbname, type, stage, column):
    uniqueness_sql  = f"SELECT (COUNT({column}) - COUNT(DISTINCT({column}))) from {type}_can{get_stagestr(stage)}"
    unique_count = get_count(cursor, uniqueness_sql)
    if unique_count == 0:
        return True
    else:
        return False


def no_nulls(cursor, dbname, type, stage, column):
    no_nulls_sql = f"SELECT COUNT({column}) from {type}_can{get_stagestr(stage)} WHERE {column} IS NULL"
    no_nulls_count = get_count(cursor, no_nulls_sql)
    if no_nulls_count == 0:
        return True
    else:
        return False


def no_blanks(cursor, dbname, type, stage, column):
    no_blanks_sql = f"SELECT COUNT({column}) from {type}_can{get_stagestr(stage)} WHERE {column} = ''"
    count_blank = get_count(cursor, no_blanks_sql)
    if count_blank == 0:
        return True
    else:
        return False


def always_value(cursor, dbname, type, stage, column, value):
    always_value_sql = f"SELECT COUNT({column}) from {type}_can{get_stagestr(stage)} WHERE {column} != {value}"
    count_value = get_count(cursor, always_value_sql)
    if count_value == 0:
        return True
    else:
        return False


def uwi_exits_ab_sk(cursor, dbname, type, stage):
    uwi_sql = f"SELECT COUNT(*) FROM {type}_can{get_stagestr(stage)} WHERE provstate in ('AB', 'SK') and uwi = ''"
    count_blank_uwi = get_count(cursor, uwi_sql)
    if count_blank_uwi == 0:
        return True
    else:
        return False


def dls_nts_validator(cursor, dbname, type, stage):
    pass


def valid_data(cursor, dbname, type, stage, column, values):
    values_in_sql = f"SELECT COUNT(*) from {type}_can{get_stagestr(stage)} WHERE {column} NOT IN {values}"
    count_values_in = get_count(cursor, values_in_sql)
    if count_values_in == 0:
        return True
    else:
        return False
