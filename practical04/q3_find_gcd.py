#Filename: q3_find_gcd.py
#author: wzx

#function
def gcd(m,n):
   if (m%n==0):
      return n;
   else:
      return gcd(n,m%n);

#main
print(gcd(24,16));
print(gcd(255,15));
