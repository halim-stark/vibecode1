expenses = []
user = 0
plus_expenses = 0

def add_one_expense(expenses):
    userAdd = input("Masukan jumlah pengeluaran: ")
    userAddInt = int(userAdd)
    print(f"{userAddInt} berhasil di tambahkan")
    expenses.append(userAddInt)
    addmore = input("Apakah anda ingin menambahkan pengeluaran lagi? ketik 'y' untuk ya atau 'n' untuk tidak. : ")
    return addmore

def add_expense(expenses):
    addmore = "y"
    while addmore =="y":
        addmore = add_one_expense(expenses)

def see_expense(expenses):
    for index, expense in enumerate(expenses, start = 1):
        print(f"{index}. {expense}")

def add_all_expenses(expenses):
    plus_expenses = 0
    for expense in expenses:
        plus_expenses += expense
    print(plus_expenses)
    return plus_expenses

def highest_expense(expenses):
    highest = max(expenses)
    print(highest)





while user != 5:
    print("=== EXPENSE ANALYZER ===")
    print("1. Tambah pengeluaran")
    print("2. Lihat pengeluaran")
    print("3. Total pengeluaran")
    print("4. Pengeluaran terbesar")
    print("5. Keluar")
    user = int(input("Pilih: "))
    if user == 1:
        add_expense(expenses)

    elif user == 2:
        see_expense(expenses)

    elif user == 3:
        add_all_expenses(expenses)

    elif user == 4:
        highest_expense(expenses)



