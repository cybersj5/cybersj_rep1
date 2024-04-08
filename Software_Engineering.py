import sqlite3

connection = sqlite3.connect('applicants_of_SoftEngineering.db')
curse_2 = connection.cursor()

curse_2.execute("""CREATE TABLE IF NOT EXISTS Software_Engineering(
                id int primary key, 
                certificate bool, 
                full_name varchar(100), 
                snils varchar(11), 
                exam_scores int)""")
connection.commit()

applicant_4 = [1, True, 'Смагин Михаил Юрьевич', '44444444444', 219]
curse_2.execute("INSERT OR IGNORE INTO Software_Engineering VALUES(?,?,?,?,?);", applicant_4)

applicant_5 = [2, True, 'Главинская Анна Павловна', '55555555555', 234]
curse_2.execute("INSERT OR IGNORE INTO Software_Engineering VALUES(?,?,?,?,?);", applicant_5)

applicant_6 = [3, False, 'Моисеев Кирилл Геннадьевич', '66666666666', 275]
curse_2.execute("INSERT OR IGNORE INTO Software_Engineering VALUES(?,?,?,?,?);", applicant_6)

curse_2.execute("SELECT * FROM Software_Engineering ORDER BY exam_scores DESC")

for i in curse_2:
    print(i)
connection.commit()