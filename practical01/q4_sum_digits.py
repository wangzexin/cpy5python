#Filename q4_sum_digits.py
#author:wzx
#Summing the digits in an integer

#main

#prompt and get the integer
integer=int(input("Enter an integer : "))
#calculate the sum
total=0
for i in range(1,4):
    total=total+integer%10
    integer=integer//10
#output
print("The sum of digits is : ",total)
