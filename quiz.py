# score = 0
# urutan_abcd = ["A", "B", "C", "D"]


# soal1 = "Apa ibu kota Indonesia?"
# jawaban1 = ["Bandung", "Jakarta", "Surabaya", "Medan"]

# print(f"Soal 1 \n{soal1}")
# for index, jawaban in enumerate(jawaban1):
#     print(urutan_abcd[index],jawaban)
# user = input("Type your answer: ").upper()

# if user == urutan_abcd[1]:
#     score += 1
#     print(f"Correct! your score: {score}")
# else:
#     print(f"incorrect, your score: {score}")



# soal2 = "Berapa hasil dari 5 + 3?"
# jawaban2 = ["6", "7", "8", "9"]

# print(f"Soal 2 \n{soal2}")
# for index, jawaban in enumerate(jawaban2):
#     print(urutan_abcd[index],jawaban)
# user = input("Type your answer: ").upper()

# if user == urutan_abcd[2]:
#     score += 1
#     print(f"Correct! your score: {score}")
# else:
#     print(f"incorrect, your score: {score}")

    
# soal3 = "Manakah yang merupakan tipe data untuk menyimpan beberapa item secara berurutan di Python?"
# jawaban3 = ["list", "int", "bool", "float"]

# print(f"Soal 3 \n{soal3}")
# for index, jawaban in enumerate(jawaban3):
#     print(urutan_abcd[index],jawaban)
# user = input("Type your answer: ").upper()

# if user == urutan_abcd[0]:
#     score += 1
#     print(f"Correct! your score: {score}")
# else:
#     print(f"incorrect, your score: {score}")


# soal4 = "Function di Python dibuat menggunakan keyword apa?"
# jawaban4 = ["fungtion", "func", "def", "make"]

# print(f"Soal 4 \n{soal4}")
# for index, jawaban in enumerate(jawaban4):
#     print(urutan_abcd[index],jawaban)
# user = input("Type your answer: ").upper()

# if user == urutan_abcd[2]:
#     score += 1
#     print(f"Correct! your score: {score}")
# else:
#     print(f"incorrect, your score: {score}")

    
# soal5 = "Index pertama sebuah Python list adalah?"
# jawaban5 = ["0", "1", "-1", "2"]

# print(f"Soal 5 \n{soal5}")
# for index, jawaban in enumerate(jawaban5):
#     print(urutan_abcd[index],jawaban)
# user = input("Type your answer: ").upper()

# if user == urutan_abcd[0]:
#     score += 1
#     print(f"Correct! your score: {score}")
# else:
#     print(f"incorrect, your score: {score}")

# print(f"Your total score is {score}/5")




# versi fungtion

# score = 0
# list_soal = ["Apa ibu kota Indonesia?","Berapa hasil dari 5 + 3?","Manakah yang merupakan tipe data untuk menyimpan beberapa item secara berurutan di Python?","Function di Python dibuat menggunakan keyword apa?","Index pertama sebuah Python list adalah?"]
# urutan_abcd = ["A", "B", "C", "D"]
# jawaban1 = ["Bandung", "Jakarta", "Surabaya", "Medan"]
# jawaban2 = ["6", "7", "8", "9"]
# jawaban3 = ["list", "int", "bool", "float"]
# jawaban4 = ["fungtion", "func", "def", "make"]
# jawaban5 = ["0", "1", "-1", "2"]

# def soal(soal,jawaban,score,jawaban_benar):
#     print(soal)
#     for index, j in enumerate(jawaban):
#         print(urutan_abcd[index], j)
#     user = input("Ketik jawaban anda: ").upper()
#     if user == jawaban_benar:
#         score += 1
#     return score

# score = soal(list_soal[0],jawaban1,score,"B")
# score = soal(list_soal[1],jawaban2,score,"C")
# score = soal(list_soal[2],jawaban3,score,"A")
# score = soal(list_soal[3],jawaban4,score,"C")
# score = soal(list_soal[4],jawaban5,score,"A")

# print(f"Your total score is {score}/5")


# versi lebih singkat lagi

# score = 0

# list_soal = ["Apa ibu kota Indonesia?","Berapa hasil dari 5 + 3?","Manakah yang merupakan tipe data untuk menyimpan beberapa item secara berurutan di Python?","Function di Python dibuat menggunakan keyword apa?","Index pertama sebuah Python list adalah?"]
# urutan_abcd = ["A", "B", "C", "D"]
# jawaban1 = ["Bandung", "Jakarta", "Surabaya", "Medan"]
# jawaban2 = ["6", "7", "8", "9"]
# jawaban3 = ["list", "int", "bool", "float"]
# jawaban4 = ["fungtion", "func", "def", "make"]
# jawaban5 = ["0", "1", "-1", "2"]
# semua_jawaban = [jawaban1,jawaban2,jawaban3,jawaban4,jawaban5]
# urutan_jawaban = ["B","C","A","C","A"]

# def soal(soal,jawaban,score,jawaban_benar):
#     print(soal)
#     for index, j in enumerate(jawaban):
#         print(urutan_abcd[index], j)
#     user = input("Ketik jawaban anda: ").upper()
#     if user == jawaban_benar:
#         score += 1
#     return score

# for i in range(5):
#     list_soal[i]
#     semua_jawaban[i]
#     urutan_jawaban[i]
#     score = soal(list_soal[i],semua_jawaban[i],score,urutan_jawaban[i])

# print(f"Your total score is {score}/5")







# # buat dari awal lagi


