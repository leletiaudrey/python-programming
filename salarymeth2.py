salary=int(input("enter salary"))
year=int(input("enter years of service"))
if year >10:
 print(salary*0.1)
if year >=6 and year<=10:
     print(salary*0.08)
if year <6:
   print( salary*0.05)