#mission: determine how long it will take you to save enough
#money to make the down payment of a house
total_cost = int(input("Enter the cost of your dream home: "))
salary = int(input("Enter your annual salary:"))
portion_saved = input("Enter the percent of your salary to save, as a decimal:")
semi_annual_raise = input("What's the semi annual rise of your salary?(decimal)")

semi_annual_raise = float(semi_annual_raise)
portion_saved = float(portion_saved)
portion_down_payment = 0.25 * total_cost

annual_salary = salary / 12

r = 0.04 / 12
#r means the return rate of investments per months(=0.04 per year)
months = 0
return_of_investments =  r + 1

current_savings = 0

x = salary / 12 * portion_saved

while current_savings < portion_down_payment:
    
    current_savings = (current_savings * return_of_investments) + x
    months += 1
    
    check_semi = months % 6
    if check_semi == 0:
        x = x * (semi_annual_raise + 1)
        
    if current_savings >= portion_down_payment:
        break

print(months)
print(x)
print(return_of_investments)
print(current_savings)



