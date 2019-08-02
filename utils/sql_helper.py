import json
import utils.connect
from prettytable import PrettyTable


def get_count(cursor, sqlquery):
    cursor.execute(sqlquery)
    row = cursor.fetchone()
    if row:
        return row[0]


def make_counts(cursor, dbname, type, stage):
    counts = []
    
    if stage == 'true':
        stagingtable = '_stage'
    elif stage == 'false':
        stagingtable = ''

    if type == 'well':
        abandon = '3'
    elif type == 'fac':
        abandon = '4'

    sql_count = f'SELECT COUNT(*) FROM {type}_can{stagingtable}'
    sql_count_unabandoned = f'SELECT COUNT(*) FROM {type}_can{stagingtable} WHERE status != {abandon}'
    sql_count_ab = f'SELECT COUNT(*) FROM {type}_can{stagingtable} WHERE status != {abandon} AND provstate = \'AB\''
    sql_count_bc = f'SELECT COUNT(*) FROM {type}_can{stagingtable} WHERE status != {abandon} AND provstate = \'BC\''
    sql_count_mb = f'SELECT COUNT(*) FROM {type}_can{stagingtable} WHERE status != {abandon} AND provstate = \'MB\''
    sql_count_sk = f'SELECT COUNT(*) FROM {type}_can{stagingtable} WHERE status != {abandon} AND provstate = \'SK\''
    sql_count_yt = f'SELECT COUNT(*) FROM {type}_can{stagingtable} WHERE status != {abandon} AND provstate = \'YT\''

    count_total = utils.sql_helper.get_count(cursor, sql_count)
    count_unabandoned = utils.sql_helper.get_count(cursor, sql_count_unabandoned)
    count_ab = utils.sql_helper.get_count(cursor, sql_count_ab)
    count_bc = utils.sql_helper.get_count(cursor, sql_count_bc)
    count_mb = utils.sql_helper.get_count(cursor, sql_count_mb)
    count_sk = utils.sql_helper.get_count(cursor, sql_count_sk)
    count_yt = utils.sql_helper.get_count(cursor, sql_count_yt)

    table = PrettyTable(['Type', 'Canada', 'Active', 'AB', 'BC', 'MB', 'SK', 'YT'])
    table.add_row([type, count_total, count_unabandoned, count_ab, count_bc,
                   count_mb, count_sk, count_yt])
    print(table)

    table_str = table.get_string()

    with open(f"counts_{dbname}_{type}{stagingtable}.txt", "w+") as f:
        f.write(table_str)

    counts.append({'type': 'Well', 'location': 'Canada', 'count': count_total})
    counts.append({'type': 'Well', 'location': 'Active', 'count': count_unabandoned})
    counts.append({'type': 'Well', 'location': 'AB', 'count': count_ab})
    counts.append({'type': 'Well', 'location': 'BC', 'count': count_bc})
    counts.append({'type': 'Well', 'location': 'MB', 'count': count_mb})
    counts.append({'type': 'Well', 'location': 'SK', 'count': count_sk})
    counts.append({'type': 'Well', 'location': 'YT', 'count': count_yt})

    with open(f"counts_{dbname}_{type}{stagingtable}.json", "w+") as j:
        j.write(json.dumps(counts))

