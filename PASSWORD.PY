import string

password=input("Enter the password for checking the strength: ")

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]
l = len(password)
score = 0

with open('common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("The password is too common. Score: 0/7")
    exit()

if l>8:
    score+=1
if l>12:
    score += 1
if l>18:
    score+=1
if l>20:
    score+=1

print(f"Password length is {str(l)}, adding {str(score)} points")

if sum(characters)>1:
    score+=1

if sum(characters)>2:
    score+=1
    
if sum(characters)>3:
    score+=1

print(f"Password has {str(sum(characters))} differents characters type {str(sum(characters)-1)} points!")

if score<4:
    print(f"Password is quite weak! Score: {str(score)}/7 ")
    
elif score == 4:
    print(f"Password is moderate strength! Score: {str(score)}/7")
    
elif score>4 and score<6:
    print(f"Password is strong but could be better! Score: {str(score)}/7")
    
elif score>6:
    print(f"Excellent Password Strength! Score: {str(score)}/7")


# print(string.ascii_uppercase)
# print(upper_case)