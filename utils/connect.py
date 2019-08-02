db_strings = {
    'warehouse': {
        'dbtype': 'postgresql',
        'server': '192.168.49.40',
        'port': '5432',
        'database': 'warehouse',
        'uid': 'gis',
        'pwd': 'gis',
    },
    'test_dbgeocoder': {
        'dbtype': 'sqlserver',
        'server': '192.168.46.35',
        'port': '1433',
        'database': 'GISData',
        'uid': 'sa',
        'pwd': 'Super@dmin818',
    },
    'dbgeocoder': {
        'dbtype': 'sqlserver',
        'server': '192.168.60.75',
        'port': '1433',
        'database': 'GISData',
        'uid': 'sa',
        'pwd': 'Super@dmin818',
    },
}


def by_database_string(database_string):
    if db_strings[database_string]['dbtype'] == 'sqlserver':
        import pyodbc
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=%s;'
                              'Database=%s;'
                              'uid=%s;'
                              'pwd=%s;' % (db_strings[database_string]['server'],
                                           db_strings[database_string]['database'], db_strings[database_string]['uid'],
                                           db_strings[database_string]['pwd']))
    elif db_strings[database_string]['dbtype'] == 'postgresql':
        import psycopg2
        conn = psycopg2.connect(user=db_strings[database_string]['uid'],
                                password=db_strings[database_string]['pwd'],
                                host=db_strings[database_string]['server'],
                                port=db_strings[database_string]['port'],
                                database=db_strings[database_string]['database'])
    cursor = conn.cursor()
    return cursor
