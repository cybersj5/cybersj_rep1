import sqlite3

connection = sqlite3.connect('applicants_of_AppInformatics.db')
curse = connection.cursor()

curse.execute("""CREATE TABLE IF NOT EXISTS applicants(
                id int primary key, 
                certificate bool, 
                full_name varchar(50), 
                snils varchar(11), 
                exam_scores int)""")
connection.commit()

applicants_list = [1, True, 'Смагин Михаил Юрьевич', '11111111111', 219]

curse.execute("INSERT INTO applicants VALUES(?,?,?,?,?);", applicants_list)
connection.commit()
