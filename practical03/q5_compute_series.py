#Filename: q5_compute_series.py
#author: wzx

#function
def m_series(i):
   print('i        m(i)');
   a=[0 for x in range(0,2*i+2)];
   a[0]=0;
   for x in range(1,i+1):
      a[x]=a[x-1]+1/(2*x-1)-1/(2*x+1);
      st=str(2*x-1);
      for y in range(1,10-len(st)+1):
         st=st+' ';
      print(st,'{0:.11f}'.format(4*a[x]));
      
#main
i=int(input('Enter a number :'));
m_series(i);
   
