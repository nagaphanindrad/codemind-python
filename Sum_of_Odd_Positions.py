n=int(input())
s1=0
arr=list(map(int,input().split()))
for i in range (n):
    if i%2!=0:
        s1+=arr[i]
print(s1)