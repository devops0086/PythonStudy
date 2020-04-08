end = str("y")
taxes = 1.13
while end != str("n"):
    cost = float(input("What is the cost? "))
    paybackterm = float(input("What is the payback term? "))
    totalcost = cost*taxes
    discountindollars=(cost-float(input("Is there a discount in dollars (if no, enter '0')? ")))*taxes
    discountinpercentages=(cost*(1-float(input("Is there a discount in percentages (if no, enter '0')? "))))*taxes
    print(discountindollars)
    print(discountinpercentages)
    if discountinpercentages > 0 == True:
        print("1st Total",str(discountinpercentages)," ","Monthly at,",str(paybackterm)," is equal to",str(discountinpercentages/paybackterm))
    elif discountindollars > 0 == True:
        print("2nd Total",str(discountindollars)," ","Months to pay back:",str(paybackterm),"; is equal to",str(discountindollars/paybackterm))
    elif (discountindollars == discountinpercentages) == True:
        print("3rd Total",str(discountindollars)," ","Months to pay back:",str(paybackterm),"; is equal to",str(discountindollars/paybackterm))
    end = str(input("Continue? press 'y' to continue, press 'n' to end: "))
    
