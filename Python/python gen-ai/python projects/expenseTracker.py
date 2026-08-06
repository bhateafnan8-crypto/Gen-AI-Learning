"""
    === Expense Tracker Application ===
        - Where we can 
            - Add Expense
            - View Expense
            - View  Total  amount
            - Delete Expense (optional)
            - Search Expense (optional)

            
    ----    planning   -----

    Project 1: Expense Tracker
            User CLI se expenses add kare, category wise dekhe, total nikale
            Covers: Functions, lists, dicts, loops, conditionals, string formatting, error handling
            Real world: Personal finance management
            Size: 1-2 din

        ----  Basic structure --- 
                User se input lo (expense name, amount, category)
                Add karo, list dikhao, total nikalo
                Loop chalao jab tak user "quit" na kare
"""

# code start here

# List of Expense .. empty list

Expenses = []


# add expense => 

def add_expense():
    
    expense_name = input("Enter your expense name => ")

    try:
        expense_amount = int(input("Enter your expense amount => "))
    except ValueError:
        print("expense amount should be a digit....")
        return
    expense_category = input("Enter your expense category => ")

    if expense_name.isdigit() or  expense_category.isdigit():
        print("expense name and expense category should not  be digit")
        return
    
    if not expense_name.strip()  or not expense_category.strip():
        print("Please fill all details !!!")
        return
    my_expense = {
        "expense_name" : expense_name,
        "expense_amount" : expense_amount,
        "expense_category" : expense_category
    }

    Expenses.append(my_expense)

# View expense => 

def view_expense():
    if not Expenses:
        print("There is no data found to display!!! , please add data!!")
        return
    for i,e in enumerate(Expenses, start=1):
        print(f"{i}. {e['expense_name']}  | {e['expense_amount'] } |  {e['expense_category']}")


# view total expense amount
def total_amount():
    if not Expenses:
        print("There is no data found to display!!! , please add data!!")
        return
    total = sum(e["expense_amount"] for e in Expenses)

    print(f"Total amount => {total}")
    # for i,e in enumerate(Expenses, start=1):
    #     print(f"{sum(e["expense_amount"])}")    

# search category wise

def search_expense():
    search_expense = input("Enter category to search => ")

    if search_expense.isdigit():
        print("search_expense should not be number")
        return
    if not Expenses:
        print("no data found!!")
        return 

    
    for i , e in enumerate(Expenses,start=1):
        if search_expense.lower() == e["expense_category"].lower():
            print(f"{e['expense_name']}  | {e['expense_amount'] } |  {e['expense_category']}") 
        

# main execution
def main():
    while True:
        print("""
                === Expense Tracker Application ===
                1) Add Expense
                2) View Expense
                3) View Total amount
                4) Search by category
                5) Exit

        """)

        choice = input("Enter your choice of execution => ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            total_amount()
        elif choice =="4":
            search_expense()
        elif choice == "5":
            print("Exiting the program !! ")
            break
        else:
            print("Invalid choice , try again !")


if __name__ == "__main__":
    main()