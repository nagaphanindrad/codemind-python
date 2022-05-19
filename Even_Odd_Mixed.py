def count(num):
    c=0
    while(num):
        c+=1
        num//=10
    return c
a=int(input())
ec=0
oc=0
b=count(a)
while(a):
    r=a%10
    if(r%2==0):
        ec+=1
    else:
        oc+=1
    a//=10
if(ec==b):
    print('Even')
elif(oc>0 and ec>0):
    print('Mixed')
else:
    print('Odd')