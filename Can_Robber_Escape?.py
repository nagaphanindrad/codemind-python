n=int(input())
arr=list(map(int,input().split()))[:n]
c=0
for i in range(0,n):
    if(arr[i]+1<=n):
        c+=1
if(c==n):
    print('YES')
else:
    print('NO')