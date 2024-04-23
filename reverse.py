n=int(input("Enter the digit: "))
rev=0
while n>0:
    r=n%10
    rev=(rev*10)+r
    n//=10
    
print("Reverse the string is: ",rev)
