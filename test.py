import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('contact.book.db')

#create a cursor
c = conn.cursor()

#crate a table
# c.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
#     )""")
# many_customers=[('wes','alan','bla'),('x','y','z'),('a','b','c')]

#elem by elem
#c.execute("INSERT INTO customers VALUES ('Marry','Brown','asdasd')")

#to all multiple
# c.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)


# query the database
c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany(3)

print(c.fetchall())








print("Command executaed succesfully...")
#commit our command
conn.commit()

#close our command
conn.close()

#DATATYPES
#NULL
#INT
#REAL = nr real
#TEXT
#BLOB =img/mp3.....
