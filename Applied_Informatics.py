import sqlite3

connection = sqlite3.connect('applicants_of_AppInformatics.db')
curse = connection.cursor()

curse.execute("""CREATE TABLE IF NOT EXISTS Applied_Informatics(
                id int primary key, 
                certificate bool, 
                full_name varchar(100), 
                snils varchar(11), 
                exam_scores int)""")
connection.commit()

applicant_1 = [1, True, 'Смагин Михаил Юрьевич', '11111111111', 219]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_1)
connection.commit()

applicant_2 = [2, True, 'Главинская Анна Павловна', '22222222222', 234]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_2)
connection.commit()

applicant_3 = [3, True, 'Федина Юлиана Викторовна', '33333333333', 225]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_3)
connection.commit()

curse.execute("""SELECT full_name, snils, exam_scores
                             FROM Applied_Informatics
                             ORDER BY exam_scores
                             DESC""")
connection.commit()
for i in curse:
    print(i)
# place = 0
# c = 0
# for i in curse:
#     c += 1
#     print(i)
#     if true:
#         print(c)
#
#     for j in i:
#         print(j)
#     print()
# connection.commit()




