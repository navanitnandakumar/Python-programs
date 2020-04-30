import random

#strings
with_special_char = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+{}[]\|;:'<>,.?/*`~"
without_special_char = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#menu
print("----- Password generator -----")
password_length = int(input("- Enter length of password --> "))
choice = input("- Do you want to include special characters? (y or n) --> ")
flag = 'Y'

#with special characters
if choice == 'y' or choice == 'Y':
    while(flag == 'y' or flag == 'Y'):
        password = "".join(random.sample(with_special_char,password_length))
        print(password)
        flag = input("- Do you want to generate one more? (y or n) --> ")
        if flag == 'n' or flag == 'N':
            break

#without special characters
if choice == 'n' or choice == 'N':
    while(flag == 'y' or flag == 'Y'):
        password = "".join(random.sample(without_special_char,password_length))
        print(password)
        flag = input("- Do you want to generate one more? (y or n) --> ")
        if flag == 'n' or flag == 'N':
            break
