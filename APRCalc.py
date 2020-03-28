borrow=int(input("How much would you like to borrow (round to nearest $100)? "))
interest_rate=float(input("What is the interest rate (in decimals) on the loan? "))
admin_cost=int(input("What is the admin cost per $100: "))
every_x_dollar=100
print("Please note the admin cost is,","$",str(admin_cost)," per, $100.")
fees=(borrow/every_x_dollar)*admin_cost
interest_exp=borrow*interest_rate
payback=14
APR=((((fees+interest_exp)/borrow)/payback)*365)*100
print(round(float(APR),2),str("%"))
