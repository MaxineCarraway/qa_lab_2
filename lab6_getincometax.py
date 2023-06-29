def getIncomeTax(salary):
    personal_allowance = 11850
    basic_rate_threshold = 34500
    higher_rate_threshold = 150000

    if salary <= personal_allowance:
        tax_amount = 0
    elif salary <= basic_rate_threshold:
        tax_amount = (salary - personal_allowance) * 0.2
    elif salary <= higher_rate_threshold:
        basic_rate_tax = (basic_rate_threshold - personal_allowance) * 0.2
        additional_tax = (salary - basic_rate_threshold) * 0.4
        tax_amount = basic_rate_tax + additional_tax
    else:
        basic_rate_tax = (basic_rate_threshold - personal_allowance) * 0.2
        higher_rate_tax = (higher_rate_threshold - basic_rate_threshold) * 0.4
        additional_tax = (salary - higher_rate_threshold) * 0.45
        tax_amount = basic_rate_tax + higher_rate_tax + additional_tax

    return tax_amount

# Testing the function
salary1 = 20000
tax1 = getIncomeTax(salary1)
print(f"Income tax for salary £{salary1}: £{tax1}")

salary2 = 50000
tax2 = getIncomeTax(salary2)
print(f"Income tax for salary £{salary2}: £{tax2}")

salary3 = 160000
tax3 = getIncomeTax(salary3)
print(f"Income tax for salary £{salary3}: £{tax3}")
