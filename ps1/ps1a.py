
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter portion of salary to be saved in %: "))/100
total_cost = float(input("Enter the cost of your dream home: "))
r= .04
current_savings = 0 
monthly_salary = annual_salary/12
down_payment = total_cost*.25
total_months = 0
while current_savings<down_payment:
    
    current_savings += current_savings*r/12
    current_savings += monthly_salary*portion_saved
    total_months=total_months+1
print(f"Number of months: {total_months}")