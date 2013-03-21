#Filename: q4_sum_series.py
#author: wzx

#function
def m_series(i):
   print('i        m(i)');
   a=[0 for x in range(1,i+2)];
   a[1]=0.5;
   print('1          0.5000');
   for x in range(2,i+1):
      a[x]=a[x-1]+x/(x+1);
      st=str(x);
      for y in range(1,10-len(st)+1):
         st=st+' ';
      print(st,'{0:.4f}'.format(a[x]));

#main
i=int(input('Enter a number :'));
m_series(i);
   
