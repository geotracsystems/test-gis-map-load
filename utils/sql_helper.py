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

    if cursor.rowcount == 1:
        row = cursor.fetchone()
        table_name, column_name = row[0], row[1]
        return table_name, column_name



def uniqueness(cursor, dbname, type, stage, column):
    uniqueness_sql  = f"SELECT (COUNT({column}) - COUNT(DISTINCT({column}))) from {type}_can{get_stagestr(stage)}"
    cursor.execute(uniqueness_sql)
    row = cursor.fetchone()
    if row[0] == 0:
        return True
    else:
        return False


def no_nulls(cursor, dbname, type, stage, column):
    no_nulls_sql = f"SELECT COUNT({column}) from {type}_can{get_stagestr(stage)} WHERE {column} IS NULL"
    cursor.execute(no_nulls_sql)
    row = cursor.fetchone()
    if row[0] == 0:
        return True
    else:
        return False


def no_blanks(cursor, dbname, type, stage, column):
    no_blanks_sql = f"SELECT COUNT({column}) from {type}_can{get_stagestr(stage)} WHERE {column} = ''"
    cursor.execute(no_blanks_sql)
    row = cursor.fetchone()
    if row[0] == 0:
        return True
    else:
        return False


