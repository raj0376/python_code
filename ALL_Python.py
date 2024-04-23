'''
#Program to check the palindrome.
s=str(input("Enter the string to check the palindrome or not."))
x=s.casefold()
rev=reversed(x)
if list(s) == list(rev):
    print("The series is PALINDROME!")
else:
    print("The series is NOT_PALINDROME!")
'''
print()
'''
#Program to define the variables.
name="Tony Stark"
age=18
print(name)
print(age)    
is_gen = "genius"
if is_gen == "genius":
    print("genius")
else:
    print("not genius")
'''
print()
'''
super_hero=input("What is your superhero name?")
print(super_hero + " Your super hero is very cool nice choice")

first=input("Enter first number: ")
second=input("Enter second number: ")
print(f"{first} + {second}", "=", int(first) + int(second))
'''
print()
'''
n=str(input("Enter any string: "))
f=str(input("Enter string to be find: "))
print(n.lower()) #lower case
print(n.upper()) #upper case
print("The string name which we have to find: ", f.find(n)) #Find the string.
r=str(input("Enter the string to be replace: "))
print("The replace string will be: ", r.replace(f"{n}",r)) #replace the str
'''
print()
'''
i=10
while i>=0:
    #print(i)
    print(i * "*")
    #i+=1
    i-=1
'''
'''
print(" Program is on constructor ")

class Ocean:
    def__init__(self,name,age):
        self.name = name
        self.age = age
c=Ocean("Jellyfish,102")
print(str(c))
print(repr(c))
'''

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
print(y)
print(y[1:3])
x = tuple(y)
print(x)