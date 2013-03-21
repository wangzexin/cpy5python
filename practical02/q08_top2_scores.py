#Filename q08_top2_scores.py
#author: wzx
#Finding the two highest scores

#main

#function for finding the highest score
def max(s,n):
   x=0
   t=0
   for i in range(1,n+1):
      if s[i]>x:
         t=i
         x=s[i]
   return t

#input&output
s=[0 for i in range(0,100)]
na=['' for i in range(0,100)]
n=int(input("Enter the number of students: "))
for i in range(1,n+1):
   na[i]=input("Enter the student's name: ")
   s[i]=int(input("Enter his/her score: "))
da=max(s,n)
print(na[da]," has the highest score: ",s[da])
s[da]=0
da=max(s,n)
print(na[da]," has the second highest score: ",s[da])
