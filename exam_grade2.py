grade = int(input("What was score on the recent exam?"))

if grade <1 or grade >  100:
    print("Error: Marks must be between 1 and 100") 
else:
    level = int(input("Please enter the student level (1 or 2)"))
    
    if level == 1:
        if grade < 50:
            print("I'm sorry, you have not passed the required mark")
        elif grade <= 60:
            print("Well done, you passed!")   
        elif grade <= 70:
            print("Superb, you have a merit!")
        else:
            print("Congratulations, you have recieved a distinction!")
    elif level == 2:
        if grade < 40:
            print("I'm sorry, you have not passed the required mark")
        elif grade <= 50:
            print("Well done, you passed!") 
        elif grade <= 65:
            print("Superb, you have a merit!")
        else:
            print("Congratulations, you have recieved a distinction!")
    else:
        print("Invalid Student Level. Please enter level 1 or 2")
            
            
    