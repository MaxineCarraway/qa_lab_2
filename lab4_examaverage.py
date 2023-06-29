# input exam marks for three subjects

math = int(input("What is your math score (0-100)? "))
while not 0 <= math <= 100:
    print("Invalid score, please enter a score between 0-100)")
english = int(input("What is your english score? (0-100) "))
while not 0 <= english <= 100:
    print("Invalid score, please enter a score between 0-100)")
ict = int(input("What is your ICT score? (0-100) "))
while not 0 <= ict <= 100:
    print("Invalid score, please enter a score between 0-100)")
# calculate average mark  
allthree = (math + english + ict) //3

# overall result
if allthree >= 65:
    result = "pass"
else:
    result = "fail"

# Display average mark and overall result
print(f"Average score: {allthree}")
print(f"Overall result: {result}")
