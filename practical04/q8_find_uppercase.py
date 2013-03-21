#Filename: q8_find_uppercase.py
#author: wzx

#function
def find_num_uppercase(st):
   if (len(st)==1):
      if (st>='A') and (st<='Z'):
         return 1;
      else:
         return 0;
   else:
      l='';
      for i in range(0,len(st)-1):
         l=l+st[i];
      if (st[len(st)-1]>='A') and (st[len(st)-1]<='Z'):
         return 1+find_num_uppercase(l);
      else:
         return find_num_uppercase(l);

#main
print(find_num_uppercase('Good MorninG!'));
