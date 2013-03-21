#Filename q7_generate_payroll.py
#author:wzx
#Payroll

#main

#prompt and get the name
name=input("Enter name: ")
#prompt and get the numtber of the hours worked weekly
now=float(input("Enter the number of the hours worked weekly: "))
#prompt and get the hourly pay rate
hpr=float(input("Enter the hourly pay rate: "))
#prompt and get the CPF contribution rate（%）
cpf=float(input("Enter the CPF contribution rate(%): "))
#output
print("Payroll statement for ",name)
print("Number of hours worked in week: ","{0:.0f}".format(now))
print("Hourly pay rate: $","{0:.2f}".format(hpr))
print("Gross play = ","{0:.2f}".format(hpr*now))
print("CPF contribution at ","{0:.0f}".format(cpf),"% = $","{0:.2f}".format(cpf/100*hpr*now))
print()
print("New pay = $","{0:.2f}".format((1-cpf/100)*hpr*now))
