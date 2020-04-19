#imports the random fn
import random   
#menu
print("-------- 🔸 Guess the number 🔸 --------")      
print(" 1. Play")
print(" 2. Exit")
option = int(input("Enter 1 or 2 --> "))
if (option == 1):
    num = random.randint(0,9)  
    #random number btwn 0 and 9 generated
    print("A random number between 0 and 9 has been generated...")
    print("Try and guess the number 😜")
    print("You have 3 chances...")
    i=0
    while(i<3):                                        
        #to count the number of attempts
        #user input
        guess = int(input("Enter your guess here --> "))           
        if(guess==num):  
            #if guess is correct
            print("WHOA!!! Congrats!!! You got it right!!! 🤩🤩🤩")      
            break                                                         
        elif(guess!=num):
            #if guess is incorrect
            print("Oops!!! You got it wrong!!! 😝😝😝")                   
            i+=1
        elif(guess>9 or guess<0):                                           
            #for invalid guess
            print("The number is between 0 and 9!!!")
        if(i == 3):
             #prints the correct number if user fails to guess
            print("The number was ",num,"!!!")                              
            print("Sorry!!! Better luck next time!!! 😊😊😊")
