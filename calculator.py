num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Calculator Menu")
print("Add (+)")
print("Subtract (-)")
print("Multiply (x)")
print("Divide (/)")
print("Square (s)")

operator = input("Choose an operation (Enter the corresponding symbol): ")

if operator == "+":
    result = num1 + num2
    print("The sum is:", result)
elif operator == "-":
    result = num1 - num2
    print("The difference is:", result)
elif operator == "x":
    result = num1 * num2
    print("The multiplied answer is:", result)
elif operator == "/":
    result = num1 / num2
    print("The divided result is:", result)
elif operator == "s":
    result1 = num1 ** 2
    result2 = num2 ** 2
    print("The square of the first number is:", result1)
    print("The square of the second number is:", result2)
else:
    print("Invalid operator. Please choose a valid operation.")