#Filename: q2_display_pattern.py
#author: wzx

#function
def count(n):
   k=1;
   s=0;
   while (k<=n):
      s=s+len(str(k))+1;
      k+=1;
   return s;

def display_pattern(n):
   l=count(n);
   for i in range(1,n+1):
      st='';
      li=count(i);
      for j in range(1,l-li+1):
         st=st+' ';
      for j in range(i,0,-1):
         st=st+str(j)+' ';
      print(st);

#main
n=int(input('Enter a number : '));
display_pattern(n);
