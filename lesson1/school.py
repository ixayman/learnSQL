import sqlite3

conn = sqlite3.connect('school.db')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS students (ID INTEGER PRIMARY KEY , name TEXT, grade INTEGER)')
cur.execute('DELETE FROM students')

students = [
    ('Alice', 82),
    ('Bob', 38),
    ('khalil', 98),
    ('john', 55),
    ('jane', 68)
]

cur.executemany('INSERT INTO students (name, grade) VALUES(?,?)', students)

cur.execute('SELECT * FROM students')
res = cur.fetchall()
for row in res:
    print(row)
print('-------------------------')
cur.execute('SELECT * FROM students WHERE grade > 80')
res = cur.fetchall()
for row in res:
    print(row)
print('-------------------------')
cur.execute('SELECT * FROM students ORDER BY NAME')
res = cur.fetchall()
for row in res:
    print(row)
print('-------------------------')
cur.execute('SELECT * FROM students ORDER BY GRADE DESC')
res = cur.fetchall()
for row in res:
    print(row)
print('-------------------------')
cur.execute('UPDATE students SET grade = 90 WHERE name = "Alice"')
cur.execute('DELETE FROM students WHERE name = "Bob"')
cur.execute('SELECT * FROM students')
res = cur.fetchall()
for row in res:
    print(row)
print('-------------------------')

conn.commit()
conn.close()
