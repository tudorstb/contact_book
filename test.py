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
many_customer=[
                    ('wes','alan','bla'),
                    ('x','y','z'),
                    ('a','b','c') ]

c.execute("INSERT INTO customers VALUES ('Marry','Brown','asdasd')")


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
