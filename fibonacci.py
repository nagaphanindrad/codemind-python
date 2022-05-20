num=int(input())
a=0
print(a,end=' ')
b=1
print(b,end=' ')
for i in range(2,num):
    c=a+b
    print(c,end=' ')
    a=b
    b=c