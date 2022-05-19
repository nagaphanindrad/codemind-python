n=int(input())
su=0
s=0
sun=0
while n>0:
    r=n%10
    su+=r
    n=n//10
while su>0:
    a=su%10
    s+=a
    su=su//10
while s>0:
    b=s%10
    sun+=b
    s=s//10
print(sun)    

   