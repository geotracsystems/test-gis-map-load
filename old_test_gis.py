import json
import utils.connect
import utils.sql_helper
from prettytable import PrettyTable


counts = []

# cursor = utils.connect.connect_db('SQL Server', '192.168.46.35', '1433', 'GISData', 'QASQLTest', 'Qa1T0sQ!')
# cursor = utils.connect.connect_db('PostgreSQL Unicode','192.168.60.75', 'GISData', 'sa', 'Super@dmin818')

# cursor = utils.connect.connect_db('postgresql', '192.168.49.40', '5432', 'warehouse', 'gis', 'gis')

cursor = utils.connect.by_database_string('warehouse')

sql_count_well_can = 'SELECT COUNT(*) FROM well_can'
sql_count_well_can_unabandoned = 'SELECT COUNT(*) FROM well_can WHERE status != 3'
sql_count_well_can_ab = 'SELECT COUNT(*) FROM well_can WHERE status != 3 AND provstate = \'AB\''
sql_count_well_can_bc = 'SELECT COUNT(*) FROM well_can WHERE status != 3 AND provstate = \'BC\''
sql_count_well_can_mb = 'SELECT COUNT(*) FROM well_can WHERE status != 3 AND provstate = \'MB\''
sql_count_well_can_sk = 'SELECT COUNT(*) FROM well_can WHERE status != 3 AND provstate = \'SK\''
sql_count_well_can_yt = 'SELECT COUNT(*) FROM well_can WHERE status != 3 AND provstate = \'YT\''

sql_count_fac_can = 'SELECT COUNT(*) FROM fac_can'
sql_count_fac_can_unabandoned = 'SELECT COUNT(*) FROM fac_can WHERE status not in (4)'
sql_count_fac_can_ab = 'SELECT COUNT(*) FROM fac_can WHERE status != 4 AND provstate = \'AB\''
sql_count_fac_can_bc = 'SELECT COUNT(*) FROM fac_can WHERE status != 4 AND provstate = \'BC\''
sql_count_fac_can_mb = 'SELECT COUNT(*) FROM fac_can WHERE status != 4 AND provstate = \'MB\''
sql_count_fac_can_sk = 'SELECT COUNT(*) FROM fac_can WHERE status != 4 AND provstate = \'SK\''
sql_count_fac_can_yt = 'SELECT COUNT(*) FROM fac_can WHERE status != 4 AND provstate = \'YT\''


count_well_can = utils.sql_helper.get_count(cursor, sql_count_well_can)
count_well_can_unabandoned = utils.sql_helper.get_count(cursor, sql_count_well_can_unabandoned)
count_well_can_ab = utils.sql_helper.get_count(cursor, sql_count_well_can_ab)
count_well_can_bc = utils.sql_helper.get_count(cursor, sql_count_well_can_bc)
count_well_can_mb = utils.sql_helper.get_count(cursor, sql_count_well_can_mb)
count_well_can_sk = utils.sql_helper.get_count(cursor, sql_count_well_can_sk)
count_well_can_yt = utils.sql_helper.get_count(cursor, sql_count_well_can_yt)

count_fac_can = utils.sql_helper.get_count(cursor, sql_count_fac_can)
count_fac_can_unabandoned = utils.sql_helper.get_count(cursor, sql_count_fac_can_unabandoned)
count_fac_can_ab = utils.sql_helper.get_count(cursor, sql_count_fac_can_ab)
count_fac_can_bc = utils.sql_helper.get_count(cursor, sql_count_fac_can_bc)
count_fac_can_mb = utils.sql_helper.get_count(cursor, sql_count_fac_can_mb)
count_fac_can_sk = utils.sql_helper.get_count(cursor, sql_count_fac_can_sk)
count_fac_can_yt = utils.sql_helper.get_count(cursor, sql_count_fac_can_yt)

table = PrettyTable(['Type', 'Canada', 'Active', 'AB', 'BC', 'MB', 'SK', 'YT'])
table.add_row(['Wells', count_well_can, count_well_can_unabandoned, count_well_can_ab, count_well_can_bc,
               count_well_can_mb, count_well_can_sk, count_well_can_yt])
table.add_row(['Facilities', count_fac_can, count_fac_can_unabandoned, count_fac_can_ab, count_fac_can_bc,
               count_fac_can_mb, count_fac_can_sk, count_fac_can_yt])

print(table)

table_str = table.get_string()

with open("counts.txt", "w+") as f:
    f.write(table_str)

counts.append({'type': 'Well', 'location': 'Canada', 'count': count_well_can})
counts.append({'type': 'Well', 'location': 'Active', 'count': count_well_can_unabandoned})
counts.append({'type': 'Well', 'location': 'AB', 'count': count_well_can_ab})
counts.append({'type': 'Well', 'location': 'BC', 'count': count_well_can_bc})
counts.append({'type': 'Well', 'location': 'MB', 'count': count_well_can_mb})
counts.append({'type': 'Well', 'location': 'SK', 'count': count_well_can_sk})
counts.append({'type': 'Well', 'location': 'YT', 'count': count_well_can_yt})
counts.append({'type': 'Facility', 'location': 'Canada', 'count': count_fac_can})
counts.append({'type': 'Facility', 'location': 'Active', 'count': count_fac_can_unabandoned})
counts.append({'type': 'Facility', 'location': 'AB', 'count': count_fac_can_ab})
counts.append({'type': 'Facility', 'location': 'BC', 'count': count_fac_can_bc})
counts.append({'type': 'Facility', 'location': 'MB', 'count': count_fac_can_mb})
counts.append({'type': 'Facility', 'location': 'SK', 'count': count_fac_can_sk})
counts.append({'type': 'Facility', 'location': 'YT', 'count': count_fac_can_yt})

with open("counts.json", "w+") as j:
    j.write(json.dumps(counts))

print("##teamcity[setParameter name='env.ddd' value='fff']")
