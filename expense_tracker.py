
expenses = []
def whatis_yourname():
    username = input("Please input name ? - ")
    return username
def quit_program(username):
    print("Goodbye " + username + " Have an expense free day")

def add_expenses():
    global expenses 
    name = input(" name of expense - ")
    amount = float(input("amount in figures - R"))
    day = (input(" dd/mm/yyyy - "))
    expenses.append({"name" : name, "amount": amount, "day": day})
    return expenses

def remove_expenses():
    global expenses
    for i in range(len(expenses)):
        print(str(i) + ". " + expenses[i]["name"])
    select = int(input("what option to delete ?"))
    expenses.pop(select)

#name = add_expenses()
#amount = add_expenses()

def view_expenses():
    global expenses
    for i in range(len(expenses)):
        print("\n" + str(i + 1) + "." + expenses[i]["name"] + " - " + "R" + str(expenses[i]["amount"]))
        print("   Date - " + str(expenses[i]["day"]))
    
         

def total_spent():
    global expenses 
    total = 0.0
    for i in range(len(expenses)):
        total = total + expenses[i]["amount"]
    return "R" + str(total)

def most_expended_items():
    global expenses 
    for i in range(len(expenses)):
        count = 0
        for j in range(len(expenses)):
            if expenses[i] == expenses[j]:
                count += 1
    print("Most expended item is " + expenses[i]["name"] + " you added it " + str(count) + " times")
    return count 

username = whatis_yourname()
print()

while True:
    print(  str(username) + "'s" + " Expense Tracker ")
    print()
    print(" 1. Add Expense")
    print(" 2. Remove Expense")
    print(" 3. View My Expenses")
    print(" 4. See Total Spent")
    print("5. Most expensed item")
    print("6. Quit tracking")
    print("\n")

    choice = int(input("Enter Your Choice "))

    if choice == 1:
        add_expenses()
    elif choice == 2:
        remove_expenses()
    elif choice == 3:
        view_expenses()
    elif choice == 4:
        print(total_spent())
    elif choice == 5:
        most_expended_items()
    elif choice == 6:
        quit_program()
    else:
        print("Invalid Option, Please Try Again")
