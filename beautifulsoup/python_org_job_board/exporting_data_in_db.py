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

sql = '''CREATE TABLE IF NOT EXISTS DETAILS(id INTEGER GENERATED ALWAYS AS IDENTITY ,\
title varchar(100) UNIQUE, location varchar(100), job_type varchar(100), posted date, category varchar(100),\
link varchar(100));'''

cursor.execute(sql)

with open('/Users/kalin/PycharmProjects/WebScrapingProject/python_org_job_board/data.csv', 'r') as f:
    cursor.copy_expert("COPY details (title, location, job_type, posted, category, link)"
                       " FROM STDIN WITH CSV HEADER "
                       "DELIMITER ','", f)

sql3 = '''select * from details;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)

conn.commit()
conn.close()
