## Get loan details from user

money_owed = float(input("How much money do you owe?\n"))
apr = float(input("What is the annual percentage rate of the loan?\n"))
payment = float(input("How much will you pay per month?\n"))
months  = int(input("How many months do you want results for?\n"))

monthly_rate = apr/100/12 #divde by 100 to get decimal & divide by 12 to get monthly int rate

for i in range(months):
    # Calculate interest
    interest_paid = money_owed*monthly_rate
    # Add in interest
    money_owed = money_owed+interest_paid

    if (money_owed - payment < 0):
        print("\nThe last payment is ", round(money_owed, 2), "dollars.")
        print("You have paid off the loan in", i+1, "months.")
        break

    # Make payment
    money_owed = money_owed - payment

    print("I paid", round(payment, 2), "of which", round(interest_paid, 2), "was interest.", end=" ")
    print("Now I owe", round(money_owed, 2), "dollars.")