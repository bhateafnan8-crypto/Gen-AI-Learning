# Question-> 
"""
1. Ek function banao jo kitne bhi numbers lo 
   aur unka average return kare — *args use karo
"""
# Soltuion-> 
print("---------------------------")
def average(*args):
    return sum(args)/len(args)

print(f"\naverage => {average(1,2,3,4,5)}\n")

import statistics

def average1(*args):
    return statistics.mean(args)

print(f"\naverage using statistics method (statistics.mean())  => {average(1,2,3,4,5)}\n")


# Question-> 
"""
2. Ek function banao jo **kwargs lo aur 
   har key-value pair print kare — 
   "Key: name, Value: Afnan" format mein
"""
# Soltuion-> 
print("---------------------------")

def showname(**kwargs):
    for key,value  in kwargs.items():
        print(f"\nkey : '{key}' , value : '{value}' \n")

showname(name="Afnan")


# Question-> 
"""
3. Dono combine karo — ek function jo 
   *args mein numbers lo aur **kwargs mein 
   label lo, aur print kare:
   "Total of [label] => [sum]"
"""
# Soltuion-> 
print("---------------------------")

def show(*args,**kwargs):
    print(f"\ntotal of {kwargs['label']} : {sum(args)}\n")

show(1,2,3,4,label="Science")


