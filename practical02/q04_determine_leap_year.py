#Filename q04_determine_leap_year.py
#author: wzx
#Determining leap year

#main

#input
y=int(input("Enter year: "))

#output
if y%4==0:
   if y%100!=0 or y%400==0:
      print("Leap")
   else:
      print("Non-Leap")
else:
   print("Non-Leap")
