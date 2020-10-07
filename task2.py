#connect with Database
import psycopg2
import sys

con = None

con = psycopg2.connect(database='testdb', user='postgres',
    password='Aleksandra08')

cur = con.cursor()
cur.execute('SELECT version()')

version = cur.fetchone()[0]
print(version)
