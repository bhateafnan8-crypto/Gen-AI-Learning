from helper import reverse_string
# Question-> 
"""
3. Create two files:
helper.py: contains function reverse_string()
main.py: import and use reverse_string() without triggering any code from helper.py
"""
# Soltuion-> 
print("---------------------------")
name = input(" enter string => " )
print(f"reverserd import from helper.py => {reverse_string(name)}")







print("====== if__name__ == __main__ ======")
if __name__ == "__main__" :
    pass 