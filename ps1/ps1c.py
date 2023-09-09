
annual_salary = float(input("Enter your annual salary: "))
annual_salary2 = annual_salary
high=10000
low = 0
portion_saved = (high+low)//2

semi_annual_raise = .07
r= .04
current_savings = 0 
monthly_salary = annual_salary/12
down_payment = 250000
steps=0

while True:

    annual_salary=annual_salary2
    current_savings=0
   
    for total_months in range(0,34):
       
        if total_months%6==0 and total_months!=0:
            annual_salary+=annual_salary*semi_annual_raise
            monthly_salary = annual_salary/12
        
        current_savings += current_savings*r/12
        current_savings += monthly_salary*portion_saved/10000
        
    steps+=1
    if abs(current_savings-down_payment)<=10:
        print(f'Best saving rate: {int(portion_saved*100)/10000}')
        print(f'Bi-section search steps: {steps}')     
        break
    if current_savings>down_payment:
        high = portion_saved
        portion_saved=(high+low)//2
        continue
    elif current_savings<down_payment:
        low = portion_saved
        portion_saved=(high+low)//2
        if portion_saved/100>=99.99:
            print("It is impossible to save for the downpayment in 3 years")
            break
        continue

