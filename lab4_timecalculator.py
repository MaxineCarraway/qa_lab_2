def add_times(time1, time2):
    days1, hours1, minutes1 = map(int, time1.split(":"))
    days2, hours2, minutes2 = map(int, time2.split(":"))
   
    total_minutes = (days1 + days2) * 24 * 60 + (hours1 + hours2) * 60 + minutes1 + minutes2
   
    new_days, remaining_minutes = divmod(total_minutes, 24 * 60)
    new_hours, new_minutes = divmod(remaining_minutes, 60)
   
    return f"{new_days:02d}:{new_hours:02d}:{new_minutes:02d}"


def find_difference(time1, time2):
    days1, hours1, minutes1 = map(int, time1.split(":"))
    days2, hours2, minutes2 = map(int, time2.split(":"))
   
    total_minutes1 = (days1 * 24 * 60) + (hours1 * 60) + minutes1
    total_minutes2 = (days2 * 24 * 60) + (hours2 * 60) + minutes2
   
    difference_minutes = abs(total_minutes1 - total_minutes2)
   
    new_days, remaining_minutes = divmod(difference_minutes, 24 * 60)
    new_hours, new_minutes = divmod(remaining_minutes, 60)
   
    return f"{new_days:02d}:{new_hours:02d}:{new_minutes:02d}"


def convert_to_hours(time):
    days, hours, minutes = map(int, time.split(":"))
    total_hours = (days * 24) + hours + minutes / 60
    return f"{total_hours:.2f}"


def convert_to_minutes(time):
    days, hours, minutes = map(int, time.split(":"))
    total_minutes = (days * 24 * 60) + (hours * 60) + minutes
    return str(total_minutes)


def convert_minutes_to_time(minutes):
    minutes = int(minutes)
    days, remaining_minutes = divmod(minutes, 24 * 60)
    hours, new_minutes = divmod(remaining_minutes, 60)
    return f"{days:02d}:{hours:02d}:{new_minutes:02d}"


def convert_hours_to_time(hours):
    hours = float(hours)
    days, remaining_hours = divmod(hours, 24)
    hours, minutes = divmod(remaining_hours * 60, 60)
    return f"{days:02d}:{hours:02d}:{minutes:02d}"


def convert_days_to_time(days):
    days = int(days)
    return f"{days:02d}:00:00"


print("Time Calculator")
print()
print("1- Add 2 times")
print("2- Find the difference between 2 times")
print("3- Convert to Hours")
print("4- Convert to Minutes")
print("5- Convert Minutes to Time")
print("6- Convert Hours to Time")
print("7- Convert Days to Time")
print("8- Exit")
print()

option = input("Enter an option: ")

while option != "8":
    if option == "1":
        time1 = input("Enter time 1 (DD:HH:MM): ")
        time2 = input("Enter time 2 (DD:HH:MM): ")
        result = add_times(time1, time2)
        print("Result:", result)
    elif option == "2":
        time1 = input("Enter time 1 (DD:HH:MM): ")
        time2 = input("Enter time")
