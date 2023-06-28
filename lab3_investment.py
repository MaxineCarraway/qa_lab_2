initial_investment = 100
target_value = 1000
interest_rate = 10

years = 0

while initial_investment < target_value:
    initial_investment += initial_investment * interest_rate
    years += 1
print(f"it will take approximately {years} years for the target amount to be reached.")