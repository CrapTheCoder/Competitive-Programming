p=[1,2,4,8,16,32,64,128,256,512,1024,2048]
for _ in range(int(input())):
    t=0
    r=int(input())
    for i in p[::-1]:
        t+=r//i 
        r%=i
    print(t)