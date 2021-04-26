import cx_Oracle
from connect_database import *

conn = connect_to_database()

c = conn.cursor()
c.execute("SELECT * FROM PFIZER_DISTRIBUTION WHERE JURISDICTION = 'Pennsylvania'")
for row in c:
    print(row[0], '-', row[1])

close_connection(conn)
