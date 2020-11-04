import psycopg2

con = psycopg2.connect(
    database='avecoder',
    user='postgres',
    password='wbtbwtb1',
    host='127.0.0.1',
    port='5432'
)

print("Database opened SUCCESSFULLY ")
cur = con.cursor()
cur.execute*(SELE)

#print('DATABASE SUCCESSFULLY')