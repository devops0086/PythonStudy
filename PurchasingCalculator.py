cost = float(input("What is the cost? "))
taxes = 1.13
paybackterm = float(input("What is the payback term? "))
totalcost = cost*taxes
discountindollars=(cost-float(input("Is there a discount in dollars (if no, enter '0')? ")))*1.13
discountinpercentages=(cost*(1-float(input("Is there a discount in percentages (if no, enter '0')? "))))*1.13

if discountinpercentages > 0:
    print("Total",str(discountinpercentages)," ","Monthly at,",str(paybackterm)," is equal to",str(discountinpercentages/paybackterm))
else:
    print("Total",str(discountindollars)," ","Months to pay back:",str(paybackterm),"; is equal to",str(discountindollars/paybackterm))

input("press enter to close:")
