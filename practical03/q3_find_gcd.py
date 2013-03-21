#Filename: q3_find_gcd.py
#author: wzx

#function

def gcd(m,n):
   if (m<n):
      swap=m;
      m=n;
      n=swap;
   while ((m%n)!=0):
      m=m%n;
      swap=m;
      m=n;
      n=swap;
   return n;

#main

print(gcd(24,16));
print(gcd(255,15));
