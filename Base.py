import sqlite3

connection = sqlite3.connect("Users.db")

curse = connection.cursor()


curse.execute("""CREATE TABLE IF NOT EXISTS Users( 
                id int auto increment primary key, 
                full_name varchar(100), 
                snils varchar(11))""")
connection.commit()

# curse.execute("SELECT * FROM Users")
#
# connection.commit()
# curse.execute("DELETE FROM Users")
# connection.commit()

for i in curse:
    print(i)


# curse.close
# connection.close









