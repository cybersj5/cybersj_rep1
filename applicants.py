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

applicant_1 = [1, True, 'Смагин Михаил Юрьевич', '11111111111', 219]
curse.execute("INSERT OR IGNORE INTO applicants VALUES(?,?,?,?,?);", applicant_1)

applicant_2 = [2, True, 'Главинская Анна Павловна', '22222222222', 234]
curse.execute("INSERT OR IGNORE INTO applicants VALUES(?,?,?,?,?);", applicant_2)

connection.commit()
