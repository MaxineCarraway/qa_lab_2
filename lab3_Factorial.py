number = int(input("please enter a number:  "))
factorial = 1

if number >= 0:
    while number > 0:
        factorial *= number
        number -= 1

    print(f"The factorial of {number} is {factorial}")
else:
    print("Factorial is not defined")