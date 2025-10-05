import random
letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~")
print("WELLCOME TO PASSWORD GENERETOR")

usr_letters = int(input("How many letters you would like in your password?\n"))
usr_symbol = int(input("How many symbols you would like in your password?\n"))
usr_number = int(input("How many Number you would like in your password?\n"))

password = []

for char in range(usr_letters):
    password.append(random.choice(letters))
for char1 in range(usr_symbol):
    password.append(random.choice(symbols))
for char2 in range(usr_number):
    password.append(random.choice(numbers))

random.shuffle(password)
passwod1 = "".join(password)
print(f'Your Password is : {passwod1}')
im = input()




    
