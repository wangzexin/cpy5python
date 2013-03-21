#Filename q02_triangle.py
#author: wzx
#Validating triangles and computing perimeter

#main

#input
a=int(input("Enter side 1: "))
c=int(input("Enter side 2: "))
b=int(input("Enter side 3: "))

#output
if a+b<=c or a+c<=b or b+c<=a:
   print("Invalid triangle!")
else:
   print("Perimeter = ",a+b+c)
