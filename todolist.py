# tasks = []
# user = 0

# #program fungtion
# def add_one_tasks(tasks):
#     user_task = input("Masukan tugas: ")
#     print("Tugas berhasil di tambah!")
#     tasks.append(user_task)
#     addmore = input("Tambah tugas lagi? type y / n :")
#     return addmore

# def add_tasks(tasks):
#     addmore = "y"

#     while addmore == "y":
#         addmore = add_one_tasks(tasks)

# def seetask(tasks):
#     for number, task in enumerate(tasks, start = 1):
#         print(f"{number}. {task}")

# def substrack_one_task(tasks):
#     seetask(tasks)
#     submore = "y"
#     sub_task = input('Adakah tugas yang ingin anda hapus (ketik "n" jika tidak ingin menghapus)? ketik angka:  ')
#     if sub_task != "n":
#         try:
#             sub_task = int(sub_task)
#         except:
#             print("Tolong masukan nomor yang valid")
#             return submore
#         sub_task_range = sub_task - 1
#         range_oftask = len(tasks)
#         if sub_task_range < range_oftask and sub_task_range > -1:
#             print(f"Berhasil menghapus {tasks[sub_task_range]}")
#             tasks.pop(sub_task_range)
#             submore = input("Apakah ingin menghapus lagi? type y / n :")
#             return submore
#         else:
#             print("Nomor tidak valid")
#             return submore
    

# def substrack_task(tasks):
#     submore = "y"

#     while submore == "y":
#         submore = substrack_one_task(tasks)

# # main program
# while user != 4:
#     print("===To Do List===")
#     print("1. Tambah tugas")
#     print("2. Lihat tugas")
#     print("3. Hapus tugas")
#     print("4. Keluar")
#     user = int(input("Pilih menu: "))
#     if user == 1:
#         add_tasks(tasks)

#     elif user == 2:
#         if tasks: #jika task memiliki isi
#             print("Tugas anda:")
#             seetask(tasks)
#             print("Anda belum memiliki tugas")

#     elif user == 3:
#         if tasks: #jika task memiliki isi
#             print("Daftar Tugas:")
#             substrack_task(tasks)
#         else:
#             print("Anda tidak memiliki daftar tugas")

        



# buat ulang versi contact list

#fungtion
contacts = []
numbers = []
def add_one_contact(contacts):
    input_contact = input("Masukan nama kontak: ").capitalize()
    input_number = input("Masukan nomor kontak: ")
    print("Kontak berhasil ditambahkan!")
    contacts.append(input_contact)
    numbers.append(input_number)
    add_again = input('Ingin menambah kontak lagi? ketik "y" atau "n": ')
    return add_again

def add_contact(contacts):
    add_again = "y"
    while add_again == "y":
        add_again = add_one_contact(contacts)

def see_contact(contacts):
    for index, contact in enumerate(contacts):
        print(contact,numbers[index])


def delete_one_contact(contacts):

    for index, contact in enumerate(contacts, start = 1):
        print(f"{index}. {contact}")
    user = input("Pilih contact yang ingin di hapus: (ketik 'n' untuk keluar) ")
    if user != "n":
        try:
            user_int = int(user)      
        except:
            print("Kamu memasukan huruf invalid")
            delete_contact(contacts)
            return

        user_range = user_int - 1
        user_len = len(contacts)
        if user_len >= user_int and user_int > 0:
            print(f"Contact {contacts[user_range]} berhasil di hapus")
            contacts.pop(user_range)
        else:
            print("Tolong ketik yang benar")
            delete_one_contact(contacts)


def delete_contact(contacts):
    delete_one_contact(contacts)



# main program
user = 0
while user != 4:
    print("===CONTACT LIST===")
    print("1. Tambah kontak")
    print("2. Lihat kontak")
    print("3. Hapus kontak")
    print("4. Keluar")
    user = int(input("Pilih: "))

    if user == 1:
        add_contact(contacts)

    elif user == 2:
        see_contact(contacts)

    elif user == 3:
        delete_contact(contacts)



