#Filename: q6_sum_digits.py
#author: wzx

#function
def sum_digits(n):
   if (n<=9):
      return n;
   else:
      return (n%10)+sum_digits(n//10);

#main
n=int(input('Enter a number : '));
print(sum_digits(n));
