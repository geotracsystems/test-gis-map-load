def get_count(cursor, sqlquery):
    cursor.execute(sqlquery)
    row = cursor.fetchone()
    if row:
        return row[0]
