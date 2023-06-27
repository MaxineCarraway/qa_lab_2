import math


def calculate_a(b_side, c_side):
    return (c_side**2 - b_side**2 )

def calculate_b(a_side, c_side):
    return (c_side**2 - a_side**2)

def calculate_c(a_side, b_side):
    return (a_side**2 + b_side**2)

print("Pythagoras' Calculator")
print("*" * 40)
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")
print("*" * 40)

choice = input("Enter your choice (1-3): ")

if choice == "1":
    b_side = float(input("Enter the length of B: "))
    c_side = float(input("Enter the length of C: "))
    a_side = calculate_a(b_side, c_side)
    print("The length of A is:", a_side)
elif choice == "2":
    a_side = float(input("Enter the length of A: "))
    c_side = float(input("Enter the length of C: "))
    b_side = calculate_b(a_side, c_side)
    print("The length of B is:", b_side)
elif choice == "3":
    a_side = float(input("Enter the length of A: "))
    b_side = float(input("Enter the length of B: "))
    c_side = calculate_c(a_side, b_side)
    print("The length of C is:", c_side)
else:
    print("Invalid choice. Please enter a number from 1 to 3.")
