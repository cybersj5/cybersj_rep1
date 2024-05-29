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

applicant_4 = [1, True, 'Смагин Михаил Юрьевич', '48924727991', 219]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_4)

applicant_5 = [2, True, 'Главинская Анна Павловна', '44485602730', 234]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_5)

applicant_6 = [3, False, 'Моисеев Кирилл Геннадьевич', '47488060462', 275]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_6)

applicant_7 = [4, True, 'Федина Юлиана Викторовна', '84956517367', 235]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_7)

applicant_8 = [5, False, 'Тихомирова Ангелина Сергеевна', '68026533916', 196]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_8)

applicant_9 = [6, False, 'Самойлов Михаил Вячеславович', '51357827528', 205]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_9)

applicant_10 = [7, True, 'Голубева Анна Егоровна', '75113651977', 167]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_10)

applicant_11 = [8, True, 'Харитонова Варвара Егоровна', '46039680278', 265]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_11)

applicant_12 = [9, False, 'Федорова Амелия Артемьевна', '75317005477', 242]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_12)

applicant_13 = [10, False, 'Виноградова Анастасия Никитична', '56772850115', 199]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_13)

applicant_14 = [11, True, 'Воронов Марк Львович', '30380774525', 176]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_14)

applicant_15 = [12, True, 'Соловьев Николай Георгиевич', '65538887127', 212]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_15)

applicant_16 = [13, True, 'Медведев Павел Артёмович', '53282082356', 214]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_16)

applicant_17 = [14, True, 'Сотников Владимир Денисович', '39695293964', 196]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_17)

applicant_18 = [15, False, 'Пономарев Артём Алексеевич', '34685838212', 190]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_18)

applicant_19 = [16, False, 'Иванов Павел Дмитриевич', '74132775249', 233]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_19)

applicant_20 = [17, False, 'Гущин Егор Романович', '57133218110', 289]
curse.execute("INSERT OR IGNORE INTO Applied_Informatics VALUES(?,?,?,?,?);", applicant_20)

connection.commit()

curse.execute("""SELECT full_name, snils, exam_scores
                             FROM Applied_Informatics
                             ORDER BY exam_scores
                             DESC""")

# curse.execute("DELETE FROM Applied_Informatics")
# connection.commit()

connection.commit()
for i in curse:
    print(i)
print(list(curse.execute("SELECT count (*) FROM Applied_Informatics"))[0][0])
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




