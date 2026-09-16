
# transactions = []
# user_input = 0

# while user_input != 4:
#     print("My expense tracker")

#     print("1. Add expense")
#     print("2. Show expenses")
#     print("3. Show total")
#     print("4. Exit")
#     user_input = int(input("Choose: "))
#     if user_input == 1:
        

#         expense_name = input("What did you spend on?")
#         expense_amount = int(input("How much did you spend?"))

#         transactions.append((expense_name,expense_amount))
            
#         addmore = input("Do you want to add another expense?")

#         while addmore == "yes":
            
#             expense_name = input("What did you spend on?")
#             expense_amount = int(input("How much did you spend?"))
#             addmore = input("Do you want to add another expense?")
#             transactions.append((expense_name,expense_amount))


#     elif user_input == 2:
#         print("Your transactions:")
#         for expense_name,expense_amount  in transactions:
             
#              print(f"{expense_name}: Rp{expense_amount}")

        
#     elif user_input == 3:    
#         total_amount = 0
#         for transaction in transactions:
#             total_amount += transaction[1]
#         print(f"Total: Rp1{total_amount}")




#versi menggunakan fungtion agar lebih sederhana
#


#all funtions
transactions = []
user_input = 0

def add_one_expenses(transactions):           
    expense_name = input("What did you spend on?")
    expense_amount = int(input("How much did you spend?"))
    transactions.append((expense_name,expense_amount))
    addmore = input("Do you want to add another expense?")
    return addmore

def add_expenses(transactions):
    addmore = "yes"  
  
    while addmore == "yes":
        addmore = add_one_expenses(transactions)

def all_expenses(trasactions):
    show_expenses = ""
    for expense_name, expense_amount in trasactions:
         show_expense = (f"{expense_name}: Rp{expense_amount}\n")
         show_expenses += show_expense
    return show_expenses


def calculate_total(transactions):
    amount = 0
    for transaction in transactions:
        amount += transaction[1]
    return amount

#main program
while user_input != 4:
    print("My expense tracker")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")
    user_input = int(input("Choose: "))
    if user_input == 1:
        add_expenses(transactions)
        

    elif user_input == 2:
        expenses_result = all_expenses(transactions)
        print("Your transactions:")
        print(expenses_result)
    
    elif user_input == 3: 
        cal_result = calculate_total(transactions)  
        print(f"Total: Rp{cal_result}")