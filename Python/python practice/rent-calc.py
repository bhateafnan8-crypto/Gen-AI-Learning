Daily_Expense = int(input("Enter your daily expense ="))
Rent = int(input("Enter rent ="))
Electricity_Bill = int(input("Enter electricity bill = "))
perunit_bill = int(input("Enter perunit bill = "))
Water_bill= int(input("Enter Waterbill ="))
Monthly_expense=int(input("Enter monthly expense ="))
persons = int(input("Enter persons ="))

total_electricity_bill = Electricity_Bill * perunit_bill

total_bill = (Rent + total_electricity_bill + Daily_Expense + Water_bill + Monthly_expense) // persons 

total_expense = print(total_bill)