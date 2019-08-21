import json
import utils.connect
from utils.sql_helper import get_stagestr
from utils.chat_helper import chat_helper
from prettytable import PrettyTable


def make_counts(cursor, dbname, type, stage):
    counts = []

    table_name = f"{type}_can{get_stagestr(stage)}"

    if type == 'well':
        abandon = '3'
    elif type == 'fac':
        abandon = '4'

    sql_count = f'SELECT COUNT(*) FROM {table_name}'
    sql_count_unabandoned = f'SELECT COUNT(*) FROM {table_name} WHERE status != {abandon}'
    sql_count_ab = f'SELECT COUNT(*) FROM {table_name} WHERE status != {abandon} AND provstate = \'AB\''
    sql_count_bc = f'SELECT COUNT(*) FROM {table_name} WHERE status != {abandon} AND provstate = \'BC\''
    sql_count_mb = f'SELECT COUNT(*) FROM {table_name} WHERE status != {abandon} AND provstate = \'MB\''
    sql_count_sk = f'SELECT COUNT(*) FROM {table_name} WHERE status != {abandon} AND provstate = \'SK\''
    sql_count_yt = f'SELECT COUNT(*) FROM {table_name} WHERE status != {abandon} AND provstate = \'YT\''

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
    # chat_helper(f"Counts in {dbname} > {type}_can{get_stagestr(stage)}")
    # chat_helper(table_str)

    with open(f"counts_{dbname}_{table_name}.txt", "w+") as f:
        f.write(table_str)

    counts.append({'type': 'Well', 'location': 'Canada', 'count': count_total})
    counts.append({'type': 'Well', 'location': 'Active', 'count': count_unabandoned})
    counts.append({'type': 'Well', 'location': 'AB', 'count': count_ab})
    counts.append({'type': 'Well', 'location': 'BC', 'count': count_bc})
    counts.append({'type': 'Well', 'location': 'MB', 'count': count_mb})
    counts.append({'type': 'Well', 'location': 'SK', 'count': count_sk})
    counts.append({'type': 'Well', 'location': 'YT', 'count': count_yt})

    with open(f"counts_{dbname}_{table_name}.json", "w+") as j:
        j.write(json.dumps(counts))

