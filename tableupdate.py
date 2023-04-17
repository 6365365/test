import psycopg2

POSTGRESS_URL ='' #add yor database url
conn = psycopg2.connect(POSTGRESS_URL)
cursor = conn.cursor()

cursor.execute('SELECT names, status FROM short_names')

results = cursor.fetchall()
for el in results:
    update_comand = f"UPDATE full_names SET status = {el[1]} WHERE names LIKE '{el[0]}.%'"
    cursor.execute(update_comand)

conn.commit()
