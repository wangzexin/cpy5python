#Filename: q6_determine_prime.py
#author: wzx

#function
def is_prime(n):
   flag=True;
   for i in range(2,int(math.sqrt(n))+1):
               if (n%i==0):
                  flag=False;
                  break;
   return flag;

#main
import math;
a=[0 for i in range(1,1002)];
k=2;
for i in range(1,1001):
   while (not is_prime(k)):
                  k+=1;
   a[i]=k;
   k+=1;
for i in range(1,1001):
                     print(a[i],end='');
                     for j in range(0,6-len(str(a[i]))):
                        print(' ',end='');
                     if (i%10==0):
                        print();
