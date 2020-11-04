import psycopg2

PASSWORD = input('Input password for DATABASE: ')
DATABASE = 'avecoder'
USER = 'postgres'
HOST = '127.0.0.1'
PORT = '5432'

conn = psycopg2.connect(
    database = DATABASE,
    user= USER,
    password= PASSWORD,
    host= HOST,
    port= PORT
)

print("Database opened SUCCESSFULLY ")


cursor = conn.cursor()
cursor.execute('SELECT * FROM employee LIMIT 10')
record = cursor.fetchall()

for row in cursor:
    print(row)

cursor.close()
conn.close()