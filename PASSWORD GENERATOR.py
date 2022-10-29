            #Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #print(len(letters))
# #print(letters[5])
password = []
for letter in range(1,nr_letters + 1):
    alphabet = len(letters)
    letter = letters[random.randint(1,alphabet - 1)]
    password.append(letter)
    print (letter)
print(password)

for symbol in range(1,nr_symbols + 1):
    character = len(symbols)
    symbol = symbols[random.randint(1,character - 1)]
    password.append(symbol)
    print (symbol)
print(password)

for number in range(1,nr_numbers + 1):
    numbs = len(numbers)
    number = numbers[random.randint(1, numbs - 1)]
    password.append(number)
    print (number)
print(password)
random.shuffle(password)
print(password)
password_new = ''.join(str(pd) for pd in password)
print(password_new)
print("Your password is: " + password_new)
#print(f"Your password is: {password}")


                #USING JOIN
# fruits=['banana', 'apple', 'orange', 'pear', 'grapes']
# s = ''.join(fruits)
# print(s)
#
# password = ['%', 'j', 's', 's', '3', '6', '(']
# sow = ''.join(str(pd)for pd in password)
#
# print(sow)









#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P