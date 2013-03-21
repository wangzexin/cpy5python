#Filename: q2_sum_series2.py
#author: wzx

#function
def sum_series(i):
   if (i==1):
      return 1/3;
   else:
      return sum_series(i-1)+i/(2*i+1);

#main
i=int(input('Enter a number : '));
print('{0:.3f}'.format(sum_series(i)));
