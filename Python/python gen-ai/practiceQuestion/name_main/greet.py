# Question-> 
"""
2. Create a script greet.py
It should take a name using input and greet the user. Make sure this only happens when the script is run directly.
"""
# Soltuion-> 
print("---------------------------")
name = input("Enter your name =>")
print("---------------------------")

def greet(name):
    return f"Hello! {name} , Welcome to pyhton gen ai course"









print("====== if__name__ == __main__ ======")
if __name__ == "__main__" :
    print(f"\n\ngreet function using input name => \n\n{greet(name)}\n\n" )