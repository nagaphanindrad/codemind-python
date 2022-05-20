n=int(input())
maxi=-999999
while(n):
    rem=n%10
    if(rem>maxi):
        maxi=rem
    n//=10
print(maxi)