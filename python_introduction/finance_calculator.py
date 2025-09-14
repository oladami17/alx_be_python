# finance_calculator.py

# Ask user to input monthly income and expenses
monthly_income = float(input("Enter your monthly income:  "))
monthly_expenses = float(input("Enter your monthly expenses:  "))

# Monthly savings
monthly_savings = monthly_income - monthly_expenses

#  Caculate savings after one year of savings with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# print Results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is:${projected_savings:.2f}.")
