import re
# Question-> 
"""
1. User se email lo — regex se 
   validate karo valid hai ya nahi
   (@ aur . hona chahiye)
"""
# Soltuion-> 
print("---------------------------")


mail = input("Enter your Email id :")

pattern = r'[\w.+-]+@[\w-]+\.[\w.-]+'

match = re.findall(pattern,mail)

print(match)

email = input("enter your mail : ")
def is_validate(email,pattern):
    emails = re.fullmatch(pattern,email)
    if emails:
        return "logged in"
        # return emails is not None
    return "Invalid email-id"

print(is_validate(email,pattern))


# Question-> 
"""
2. Ek string se sab phone numbers 
   nikalo — findall() use karo
   "Call 9876543210 or 8765432109"
"""
# Soltuion-> 
print("---------------------------")

phone = "Call 9876543210 or 8765432109"

patterns = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

matches = re.findall(patterns,phone)

print(matches)

p2 = r'\d{10}'

m2 = re.findall(p2,phone)

print(m2)


# Question-> 
"""
3. User se paragraph lo — 
   sab digits ko "*" se replace karo
   re.sub() use karo
"""
# Soltuion-> 
print("---------------------------")

para = input("Enter a para : ")

pattern1 = r'\d+'

match1 = re.sub(pattern1,"*",para)

print(match1)





# reg.py


#  wrong because lack of knowledege

    # mail = input("Enter your Email id :")

    # pattern = r'[\w.+-]+@[\w-]+\.[\w.-]+'

    # match = re.search(pattern,mail)

    # if match:
    #     print(match.groupdict())
