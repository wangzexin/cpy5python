#Filename: q1_sum_series1.py
#author: wzx

#function
def sum_series(i):
   if (i==1):
      return 1;
   else:
      return sum_series(i-1)+1/i;

#main
n=int(input('Enter a number : '));
print('{0:.3f}'.format(sum_series(n)));
