History_file = "history.txt"

def show_history():
    try:
        with open(History_file, "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("Not found!")
            else:
                print("--- History ---")
                for i in reversed(lines):
                    print(i.strip())
    except FileNotFoundError:
        print("No history file found!")

def clear_history():
    open(History_file, "w").close()
    print("History cleared!")

def save_history(equation, result):
    with open(History_file, "a") as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_inp):
    parts = user_inp.split()
    if len(parts) != 3:
        print("Invalid Input, Use format: number operator number (e.g. 1 + 2)")
        return

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Divider cannot be 0")
            return
        result = num1 / num2
    else:
        print("Invalid operator, use only (+ - * /).")
        return

    if int(result) == result:
        result = int(result)
    print("Result:", result)

    save_history(user_inp, str(result))

def main():
    print("--- Simple Calculator ---")

    while True:
        user_inp = input("Enter calculation (+ - * /) or command (show, clear, exit): ").strip()
        if user_inp == "exit":
            print("Have a nice day!")
            break
        elif user_inp == "show":
            show_history()
        elif user_inp == "clear":
            clear_history()
        else:
            calculate(user_inp)

main()

"""History_file = "history.txt"

def show_history():
    file = open("History_file","r")
    lines = file.readline()
    if len(lines) == 0:
        print("Not found!")
    else:
        for i in reversed(lines):
            print(lines.strip())
    file.close()



def clear_history():
    file = open("History_file","w")
    file.close()
    print("History cleared!")

def save_history(equation,result):
    file = open("History_file","a")
    file.write(equation + "=" + result + "\n")
    file.close()

def calculate(user_inp):
    parts = user_inp.split()
    if len(user_inp) != 3:
        print("Invalid Input , Use format number operator number (eg > 1 + 2). ")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1+num2
    elif op == "-":
        result = num1+num2
    elif op == "*":
        result = num1*num2
    elif op == "/":
        if num2 == 0:
            print("Divider cannot be 0")
            return
        result = num1/num2
    else:
        print("Invalid opertor, use only (+ - * /0).")

    if int(result) == result:
        result = int(result)
    print("Result:",result)

    save_history (user_inp,result,result)

def main():
    print("--- Simple Calcultor --- ")

    while True:
        user_inp = input("Enter Calculation (+ - * /) or command(show clear exit):")
        if user_inp == "exit":
            print("Have a nice day")
            break
        elif user_inp == "show":
            show_history()
        elif user_inp == "clear":
            clear_history()
        else:
            calculate(user_inp)
main() 
"""