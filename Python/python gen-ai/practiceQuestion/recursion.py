# Question-> 
'''
1. Write a recursive function power(base, exp) to compute base^exp.
'''
# Soltuion-> 
print("---------------------------")
def power(base,exp):
    if exp == 0:
        return 1
    return base * power(base,exp-1)
print(f"power of base-2 to exp-2 => {power(2,2)}")           
print(f"power of base-2 to exp-4 => {power(2,4)}")     



# Question-> 
'''
2. Write a recursive function to count digits in a number.
Example: count_digits(1234) → 4
'''
# Soltuion-> 
print("---------------------------")
def count_digits(s):
    if s == 0:
        return 0
    return 1 + count_digits(s//10)
print(f"count of digit or len of digit => {count_digits(1234)}")
print(f"count of digit or len of digit => {count_digits(123456)}")



# Question-> 
'''
3. Create a function is_palindrome(s) that checks if a string is a palindrome using recursion.
'''
# Soltuion-> 
print("---------------------------")
def is_palindrome1(s):
    if len(s) <=1 :
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome1(s[1:-1])
print(F"palindrome 1 => {is_palindrome1("121")}")

def is_palindrome2(s,r):
    if s == 0:
        return r
    return is_palindrome2(s//10 , r * 10 + ( s % 10 ))

num = int(input("enter number to check isPalindrome or not => "))
original = num

rev = is_palindrome2(num,0)
print(f"plaindrome 2 => {original == rev}")




# Question-> 
'''
4. Write a recursive function sum_of_digits(n) that returns the sum of all digits in a number.
'''
# Soltuion-> 
print("---------------------------")
def  sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits( n // 10)
print(f"sum of digit => {sum_of_digits(122)}")


# Question-> 
'''
5. Challenge: Solve Tower of Hanoi for n disks and print steps.

def hanoi(n, source, destination, helper):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n-1, source, helper, destination)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, helper, destination, source)

hanoi(3, 'A', 'C', 'B')
'''
# Soltuion-> 
print("---------------------------")

def hanoi(n, source, destination, helper):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n-1, source, helper, destination)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n-1, helper, destination, source)

print(f"tower of hanoi => {hanoi(3, 'A', 'C', 'B')}")
print (f"""steps => [a.b.c -> a.c.b -> a.b.c ->
c.b.a -> a.c.b -> b.a.c ->
b.c.a -> a.c.b ->]""")