# Task 7 - Income Tax Calculator Thalersland

income = float(input("Enter the amount of money you earn: "))
tax_amount = 0.0

if not income > 85_528:
    tax_amount = (income * 0.18) - 556.2
else:
    tax_amount = ((income - 85_528) * 0.32) + 14_839

print("\nYour annual tax is: ", float(round(tax_amount)))
