ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

length = len(ages)
print("Length of ages List:", length)
print("*" * 40)

# Exercise 2
print("Ages:")
for age in ages:
    print(age)
print("*" * 40)

# Exercise 3
for i in range(length):
    ages[i] += 1

print("Ages after adding one year:")
for age in ages:
    print(age)
print("*" * 40)

# Exercise 4
for i in range(length-1, -1, -1):
    if ages[i] < 16 or ages[i] > 65:
        del ages[i]

print("Ages after removing ages outside 16-65 range:")
for age in ages:
    print(age)
print("*" * 40)

# Exercise 5
count_16_25 = 0
for age in ages:
    if age >= 16 and age <= 25:
        count_16_25 += 1

print("Count of 16-25 year olds:", count_16_25)
print("*" * 40)

# Exercise 6
ages.sort()
print("Ages after sorting:")
for age in ages:
    print(age)
print("*" * 40)

# Exercise 7
count_between_16_25 = 0
for age in ages:
    if age >= 16 and age <= 25:
        count_between_16_25 += 1

proportion = count_between_16_25 / length
print("Proportion of ages between 16-25:", proportion)