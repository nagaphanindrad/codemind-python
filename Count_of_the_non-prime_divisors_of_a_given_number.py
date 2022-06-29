def prime(num):
    if(num==1):
        return True
    else:
        for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                return True
    return False
a=int(input())
c=0
for i in range(1,a+1):
    if(a%i==0 and prime(i)):
        c+=1
print(c)