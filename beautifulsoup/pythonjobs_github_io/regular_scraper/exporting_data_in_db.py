import psycopg2
import os

from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    database="web_scraping_db",
    user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'),
    host='127.0.0.1', port='5432'
)

conn.autocommit = True
cursor = conn.cursor()

sql = '''
CREATE TABLE IF NOT EXISTS pythonjobs_iogithub(id INTEGER GENERATED ALWAYS AS IDENTITY,
title varchar(100) UNIQUE, location varchar(100), posted date, role varchar (100),
job_details varchar(200), link varchar(100))
'''

cursor.execute(sql)

with open('../data.csv', 'r') as f:
    cursor.copy_expert(
        "COPY pythonjobs_iogithub (title, location, posted, role, job_details, link)" 
        " FROM STDIN WITH CSV HEADER "
        "DELIMITER ','", f)

sql2 = '''select * from pythonjobs_iogithub;'''
cursor.execute(sql2)
for i in cursor.fetchall():
    print(i)


conn.commit()
conn.close()