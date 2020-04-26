import time
import winsound

#title
print("----- Alarm -----")

#alarm fn
def my_alarm():
    try:
        
        my_time = list((map(int,input("- Enter time in 'hr min sec' --> ").split())))
        
        #valid input case
        if len(my_time) == 3:
            total_seconds = my_time[0]*60*60 + my_time[1]*60 + my_time[2]
            print("- You will be reminded after ",total_seconds," seconds...")
            time.sleep(total_seconds)
            winsound.Beep(2500,500)
        
        #invalid input case
        else:
            print("- Invalid input!")
            my_alarm()
    
    #exception case
    except Exception as e:
        print("- Exception case",e,"!")
        my_alarm()

my_alarm()
