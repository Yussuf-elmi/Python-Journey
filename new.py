# income
YOUR_NAME = input("Enter your full name:")
Salary = float(input("Enter monthly salary:"))
Other_income = float(input("Enter other monthly income:"))

# Expenses
Rent = float(input("Enter monthly rent:"))
Food = float(input("Enter Monthly food exepnses:"))
Transport = float(input("Enter monthly transport exepnses:"))
Entertainment = float(input("Enter monthly entertainment expenses:"))

# calculations
Total_Income = Salary + Other_income
Total_Expenses = Rent + Food + Transport + Entertainment
Monthly_Savings = Total_Income - Total_Expenses
Yearly_Savings = Monthly_Savings * 12
Saving_rate = (Monthly_Savings/Total_Income)*100
# Output
print("Your total monthly Income:", Total_Income)
print("Your total monthly expenses:", Total_Expenses)
print("Your monthly savings is:", Monthly_Savings)
print("Your yearly Savings is :", Yearly_Savings)
print("Your saving rate is:", Saving_rate, "%")
print("Name:", YOUR_NAME)
print("\033[92mThank you for trusting us with your financial calculations!\033[0m")
