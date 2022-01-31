print("ELIGIBLE TO VOTE")
citizen=str(input("Enter citizenship:"))
age=int(input("Enter age:"))
if citizen == "KENYAN" and age >=18:
        print("can vote")
else:
        print("can't vote")


        
country=str(input("enter country:"))
age=int(input("enter age:"))
country=["Kenya","Uganda","Tanzania","Rwanda"]
if country in country and age >=18:
    print("can vote")
else:
    print("can't vote")