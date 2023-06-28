min_val = 1
max_val = 100
tries = 0

while tries < 3:
    value = input(f"enter an integer between {min_val} and {max_val}:  ")
    if value.isdigit():
        num = int(value)
        if min_val <= num <= max_val:
            print("This is a valid entry", num)
            break
    tries += 1
    
if tries == 3:
    print("None of your entries were valid")