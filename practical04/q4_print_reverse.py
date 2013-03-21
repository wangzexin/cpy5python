#Filename: q4_print_reverse.py
#author: wzx

#function
def reverse_int(n):
   m=int(n);
   st=str(m//10);
   if (len(n)>1):
      return n[len(n)-1]+reverse_int(st);
   else:
      return n;

#main
n=input('Enter a number : ');
print(reverse_int(n));
