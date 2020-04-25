import time

#title
print('----- Python ATM -----')
restart = 'Y'
chances = 3
balance = 1000.00

#to limit PIN entry to 3 times
while chances >= 0:
    #user PIN input
    pin = int(input("- Please enter your 4 digit PIN --> "))
    #default PIN value set to '0000'
    if pin == (0000):
        print("- Correct PIN")
        #menu
        print("- MENU -")
        print(" - Press 1 for your balance")
        print(" - Press 2 to make a withdrawal")
        print(" - Press 3 to pay in")
        print(" - Press 4 to return card")

        #user input
        option = int(input("- Enter choice --> "))

        #1 --> balance
        if option == 1:
            print("- Your balance is $",balance)
            restart = input("- Would you like to go back to menu? --> ")
            if restart in ('n','N','no','NO','No'):
                print("----- Thank You -----")
                break

        #2 --> withdrawal
        elif option == 2:
            withdrawal = float(input("- How much would you like to withdraw?"
                                     "10,20,40,60,80,100 (enter the number) for other amount, enter 1 --> "))
            if withdrawal in [10,20,40,60,80,100]:
                balance = balance - withdrawal
                print("- Your balance is now $",balance)
                restart = input("- Would you like to go back to menu? --> ")
                if restart in ('n', 'N', 'no', 'NO', 'No'):
                    print("----- Thank You -----")
                    break
            elif withdrawal != [1,10,20,40,60,80,100]:
                print("- Invalid amount!")
                restart = 'Y'
            elif withdrawal == 1:
                withdrawal = float(input("- Enter desired amount --> "))
                balance = balance - withdrawal
                print("- Your balance is now $", balance)
                restart = input("- Would you like to go back to menu? --> ")
                if restart in ('n', 'N', 'no', 'NO', 'No'):
                    print("----- Thank You -----")
                    break

        #3 --> pay in
        elif option == 3:
            pay_in = float(input("- How much would you like to pay in? --> "))
            balance = balance + pay_in
            print("- Your balance is now $", balance)
            restart = input("- Would you like to go back to menu? --> ")
            if restart in ('n', 'N', 'no', 'NO', 'No'):
                print("----- Thank You -----")
                break

        #4 --> return card
        elif option == 4:
            print("- Please wait while your card is being returned...")
            time.sleep(3)
            print("----- Thank You -----")
            break

        #return case
        else:
            print("- Invalid input!")
            restart = 'Y'

    #invalid pin
    elif pin != (0000):
        print("- Invalid PIN!")
        chances = chances-1
        #if chances exhausted
        if chances == 0:
            print("- You have entered incorrect PIN 3 times!")
            print("----- Thank You -----")
            break
