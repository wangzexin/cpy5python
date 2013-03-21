#Filename: q7_find_largest.py
#author: wzx

#function
def find_largest(alist):
   a=alist.pop(len(alist)-1);
   if (len(alist)!=0):
      return max(a,find_largest(alist));
   else:
      return a;

#main
print(find_largest([5,2,7,8,1]));
