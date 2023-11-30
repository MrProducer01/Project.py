import random

n=int(input("How many numbers do you want tot set in your password?"))
c=int(input("How many letters do you want tot set in your password?"))
s=int(input("How many characters do you want tot set in your password?"))
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] + ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
r=random.random()
password =""
for i in range(n):
    password+=r.choice(characters[:30])
for i in range(c):
    password+=r.choice(numbers[:30])
for i in range(s):
    password+=r.choice(symbols[:30])
print(password)