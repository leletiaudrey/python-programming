sub1=int(input("enter subject one:"))
sub2=int(input("enter subject two:"))
sub3=int(input("enter subject three:"))
sub4=int(input("enter subject four:"))
sub5=int(input("enter subject five:"))
score=(sub1+sub2+sub3+sub4+sub5)/5
if score >=70 and score <=100:
    print("A")
elif score >=60 and score <=69:
    print("B")
elif score >=50 and score <=59:
    print("C")
elif score >=40 and score <=49:
    print("D")
else:
    print("Fail")