#Filename q07_miles_to_kilometres.py
#author: wzx
#Conversion from miles to kilometres

#main

#output
print("Miles       Kilometers          Kilometers          Miles")
for i in range(1,7):
   print(i,"            ","{0:.3f}".format(i*1.609),"                   ",i*5+15,"                       ","{0:.3f}".format(i*5*1.609+15*1.609))
for i in range(7,10):
   print(i,"            ","{0:.3f}".format(i*1.609),"                 ",i*5+15,"                       ","{0:.3f}".format(i*5*1.609+15*1.609))
print(10,"          ","{0:.3f}".format(10*1.609),"                 ",65,"                       ","{0:.3f}".format(40.398))
