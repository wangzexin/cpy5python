#Filename q12_find_factors.py
#author: wzx
#Finding the factors of an integer

#main

#function for factors
def factors(n,t,k):
   u=n
   k=1
   p=2
   while True:
      if u==1:
         break
      while True:
         if u%p==0:
            break
         p+=1
      t[k]=p
      k=k+1
      u=u//p

#input
n=int(input("Enter a number: "))

#output
t=[0 for i in range(0,n+2)]
k=1
factors(n,t,k)
while True:
   if t[k]==0:
      break
   k+=1
print("The factors are:")
for i in range(1,k-1):
   print(t[i],end=", ")
print(t[k-1],end="")
print(".")

