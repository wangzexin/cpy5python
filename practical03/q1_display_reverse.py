#Filename: q1_display_reverse.py
#author: wzx

#function

def reverse_int(n):
    st=str(n);
    rst='';
    for i in range(0,len(st)):
        rst=rst+st[len(st)-1-i];
    return rst;

#main

n=int(input('Enter a number : '));
print(reverse_int(n));
