import csv

data = [["Ford Motor Company", 16629, 10390, 40755, 18074, 19892, 22049, 17049, 10764],
["Volkswagen UK", 13224, 7960, 38335, 15161, 15737, 20474, 15183, 11334],
["Mercedes-Benz UK", 12249, 6088, 33536, 11739, 14431, 14947, 12056, 5040],
["Vauxhall Motors", 12250, 4905, 37769, 10639, 13461, 15540, 10398, 4864],
["BMW", 9553, 6870, 30330, 10868, 12415, 19985, 9198, 4853]]

filename = "car_sales.csv"

with open(filename, "w", newline = "") as file:
    writer= csv.writer(file)
    writer.writerow(data)

print("Data written to ", filename)

companies = []
sales = []

with open("car_sales.csv", "r") as file:
    lines = file.readlines()

for line in lines:
    if line.strip() == "" or line.startswith("#"):
        continue

columns = line.strip().split(",")

if len(columns) == 1:
    company = columns[0].replace('"', "").replace("\\", "")
    companies.append(company)
else:
    sales_data = [int(sale.strip) for sale in columns[1:1]]
    sales.append(sales_data)

monthly_sales_sum = []
for month_sales in zip(*sales):
    month_sum = sum(month_sales)
    monthly_sales_sum.append(month_sum)
    
yearly_sales_sum = []
for i in range(len(companies)):
    company_sales = sales[i]
    
    company_sum = sum(company_sales)
    yearly_sales_sum.append(company_sum)
    
for i in range(len(companies)):
    print(f"{companies[i]} - Monthly Sales: {monthly_sales_sum[i]}")
    print(f"{companies[i]} - Yearly Sales: {yearly_sales_sum[i]}")
    print()

grand_total = sum(yearly_sales_sum)
print("Grand total:", grand_total)
    
