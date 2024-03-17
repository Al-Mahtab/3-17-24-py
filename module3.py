#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
usr_letters=int(input('How many letters do you want in your password? '))
usr_numbers=int(input('Howmany numbers do you want in your password '))
usr_symbols=int(input('How many symbols do you need in your password? '))

password=[]
for x in range (0,usr_letters+1):
    password+=random.choice(letters)

for x in range(0,usr_numbers+1):
    password+=random.choice(symbols)

for x in range(0, usr_symbols+1):
    password+=random.choice(numbers)

random.shuffle(password)
final_pass=''
for x in password:
    final_pass+=x
print(f'Your password is {final_pass}')