import random                                    #imports the random fn
print("-------- 🔸 Guess the number 🔸 --------")      #menu
print(" 1. Play")
print(" 2. Exit")
option = int(input("Enter 1 or 2 --> "))
if (option == 1):
    num = random.randint(0,9)                        #random number btwn 0 and 9 generated
    print("A random number between 0 and 9 has been generated...")
    print("Try and guess the number 😜")
    print("You have 3 chances...")
    i=0
    while(i<3):                                        #while loop to count the number of attempts
        guess = int(input("Enter your guess here --> "))           #user input
        if(guess==num):                                  
            print("WHOA!!! Congrats!!! You got it right!!! 🤩🤩🤩")       #if guess is correct
            break                                                          #to break out of the loop, in case of correct guess
        elif(guess!=num):
            print("Oops!!! You got it wrong!!! 😝😝😝")                   #if guess is incorrect
            i+=1
        elif(guess>9 or guess<0):                                           #for invalid guess
            print("The number is between 0 and 9!!!")
        if(i == 3):
            print("The number was ",num,"!!!")                               #prints the correct number if user fails to guess
            print("Sorry!!! Better luck next time!!! 😊😊😊")