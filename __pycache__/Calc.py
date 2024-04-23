'''
#Using Module 'import'
from Calc import *

a=8
b=9

c=sum(a,b)
print("The sum of two no. is: ",c)
'''

'''
# Using class
class computer:
    def __init__(self):
        print("in init")
    
    def config(self):
        print("i5, 15gb, 1tb")
        

com1=computer()
com2=computer()

computer.config(com1)
computer.config(com2)

com1.config()

print(type(com1))
'''
'''
class computer:
    pass
    def __init__(self):
        self.name='Navin'
        self.age='18'
        

c1=computer()
c2=computer()

c1.name="Amsn"

print(c1.name)
print(c1.age)

print("Address of c1 memory: ",(id(c1)))
'''
'''
my_information = list(("Dionysia",27,True,"Lemonaki",7,"Python",False))
print(my_information)
print("\ntype of my_information variable ") 
print(type(my_information))
'''
# a=int(input("enter a num:"))
# b=int(input("enter a num:"))
x = lambda a,b: a -b +10
print(x(a,b))

# list1 = ["key1","key2","key3"]
# list2 = ["value1","value2","value3"]
# print(list1)
# print(list2)
# mydict = zip(list1,list2)	# using zip() function we can create dictionary with two lists(one list for keys and one list for values)
# print(dict(mydict))
# # convert dictionary into set using set() method
# set1=set(mydict)
# #print(dict(list1,list2) for list1, list2 in list)
# print(sorted(set1))
y="gtf"
print(type(y))
# print elements in  sorted order