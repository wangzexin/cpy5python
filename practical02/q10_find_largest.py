#Filename q10_find_largest.py
#author: wzx
#Finding the largest n such that n3 < 12000

#main

#output
n=100
while True:
   if n**3<12000:
      break
   n-=1

#output
print("The largest integer n such that n3 is less than 12,000 is: ",n)
