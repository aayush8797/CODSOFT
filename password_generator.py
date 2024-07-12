#password generator
import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = ['!','#','@','$','%','^','&','*','(',')','-','+','_',]

print("Welcome to the password generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list=[]

for char in range(1,nr_letters+1):
    password_list += random.choice(letters)

for char in range(1,nr_numbers+1):
    password_list += random.choice(numbers)

for char in range(1,nr_symbols+1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is : {password}")