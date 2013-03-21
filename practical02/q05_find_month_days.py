#Filename q05_find_month_days.py
#author: wzx
#Finding the number of days in a month

#main

#input
y=int(input("Enter year: "))
m=int(input("Enter month: "))

#output
md=[31,28,31,30,31,30,31,31,30,31,30,31]
if m==2:
   if y%4==0 and y!=100:
      md[1]+=1
   elif y%400==0:
      md[1]+=1
mm=["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
print(mm[m-1]," ",y," has ",md[m-1]," days.")
