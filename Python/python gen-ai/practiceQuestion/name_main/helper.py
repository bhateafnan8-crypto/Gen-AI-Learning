# Question-> 
"""
3. Create two files:
helper.py: contains function reverse_string()
main.py: import and use reverse_string() without triggering any code from helper.py
"""
# Soltuion-> 
print("---------------------------")
print("---------------------------")

def reverse_string(name):
    str = name
    return str[::-1]










print("====== if__name__ == __main__ ======")
if __name__ == "__main__" :
    name = input("Enter string to reverse =>")
    print(f"rerversed while only in helper.py => {reverse_string(name)}")