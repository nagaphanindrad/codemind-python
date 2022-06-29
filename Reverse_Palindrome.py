def reverse(num):
    rev=0
    while(num):
        rev=rev*10+(num%10)
        num//=10
    return rev
def palin(num):
    temp=num
    rev=0
    while(num):
        rev=rev*10+(num%10)
        num//=10
    if(temp==rev):
        return True
    else:
        return False
x=int(input())
while(True):
    x=x+reverse(x)
    if(palin(x)):
        print(x)
        break