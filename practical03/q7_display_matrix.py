#Filename: q7_display_matrix.py
#author: wzx

#function
def print_matrix(n):
   for i in range(1,n+1):
      for j in range(1,n+1):
         print(int(random.random()*2),end='  ');
      print();

#main
import random;
n=int(input('Enter a number : '));
print_matrix(n);
