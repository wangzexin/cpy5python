#Filename: q5_count_letter.py
#author: wzx

#function
def count_letter(st,ch):
   if (len(st)==1):
      if (st==ch):
         return 1;
      else:
         return 0;
   else:
      l='';
      for i in range(0,len(st)-1):
         l=l+st[i];
      if (st[len(st)-1]==ch):
         return count_letter(l,ch)+1;
      else:
         return count_letter(l,ch);

#main
print(count_letter('Welcome','e'));
