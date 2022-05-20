def count(num):
    c=0
    while(num):
        c+=1
        num//=10
    return c
a=int(input())
f=0
t=a
l=count(a)
while(a):
    c=0
    temp=t
    r=a%10
    while(temp):
        if(temp%10==r):
            c+=1
        temp//=10
    if(c==1):
        f+=1
    a//=10
if(f==l):
    print('Unique Number')
else:
    print('Not Unique Number')