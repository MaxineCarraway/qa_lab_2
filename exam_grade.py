grade = int(input("What was score on the recent exam?"))

if grade <1 or grade >  100:
    print("Error: Marks must be between 1 and 100") 
elif grade <50:
    print("I'm sorry, you have not passed the required mark")
elif grade <= 60:
    print("Well done, you passed!")   
elif grade <= 70:
    print("Superb, you have a merit!")
else:
    print("Congratulations, you have recieved a distinction!")
    
    