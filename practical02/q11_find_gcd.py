#Filename q11_find_gcd.py
#author: wzx
#Computing the greatest common divisor

#main

#input
n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))
if n1>=n2:
   d=n2
else:
   d=n1
while True:
   if n1%d==0 and n2%d==0:
      break
   d-=1

#output
print("The greatest common divisor is: ",d)
