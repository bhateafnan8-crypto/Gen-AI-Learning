# Question-> 
"""
1. Create a function that accesses a global variable and prints it.
"""
# Soltuion-> 
print("---------------------------")


global_var = "I am value of a global variable"

def globalFun():
    print(f"value of global variable => {global_var}")
globalFun()



# Question-> 
"""
2. Try modifying a global variable inside a function without using global — what happens?
"""
# Soltuion-> 
print("---------------------------")


var_global = "hello"

def fun_global():
    print(f"{var_global.replace("hello","Hey")}")
    var_global = "heyylo"
    print(f"modify wiht like this => {var_global}")


fun_global()
""" answer => Traceback (most recent call last):
  File "D:\Gen Ai\python\python gen-ai\practiceQuestion\scope.py", line 32, in <module>
    fun_global()
    ~~~~~~~~~~^^
  File "D:\Gen Ai\python\python gen-ai\practiceQuestion\scope.py", line 28, in fun_global
    print(f"{var_global.replace("hello","Hey")}")
             ^^^^^^^^^^ """