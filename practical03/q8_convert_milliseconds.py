#Filename: q8_convert_milliseconds.py
#author: wzx

#function
def convert_ms(n):
   ts=n//1000;
   s=ts%60;
   m=(ts//60)%60;
   h=ts//3600;
   st=str(h)+':'+str(m)+':'+str(s);
   return st;

#main
print(convert_ms(555550000));
