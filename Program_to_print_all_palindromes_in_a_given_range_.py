def palin(num):
    temp=num
    rev=0
    while(num):
        r=num%10
        rev=rev*10+r
        num//=10
    if(temp==rev):
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(palin(i)):
        print(i,end=" ")