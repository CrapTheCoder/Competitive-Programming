for i in range(int(input())):
    l=input().split()
    a,b,n=map(int,l)
    if n%2==0:
        a=abs(a)
        b=abs(b)
    if a>b:print(1)
    elif a<b:print(2)
    else:print(0)