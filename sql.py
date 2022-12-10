import psycopg2
import pandas as pd

# connect to the database
conn = psycopg2.connect(
    user='postgres', password='admin',
    host='localhost', database='postgres', port='5432'
)

# create a cursor to execute queries
cur = conn.cursor()


sql = '''CREATE TABLE ticker_data(datetime DATE NOT NULL,\
close FLOAT(8),\
high FLOAT(8), \
low FLOAT(8), \
open FLOAT(8), \
volume INT, \
instrument  VARCHAR(8));'''


cur.execute(sql, conn)

sql2 = '''COPY ticker_data(datetime,close,\
high,low, open,volume,instrument)
FROM '/private/tmp/data.csv'
DELIMITER ','
CSV HEADER;'''


cur.execute(sql2)

# commit the changes to the database
conn.commit()

# close the cursor and connection
cur.close()
conn.close()
