print("CLIENT 5% DISCOUNT OF GOODS ABOVE ksh1000")
amount=int(input("enter the total amount of goods bought:"))
discount = 0.05*amount
if amount >=1000:
    print("discount is",discount)
else:
    print ("no discount")