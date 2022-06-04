n = int(input())
 
lis = list(map(int, input().split()))
 
for i in range(n):
    if lis[i] % 2 == 0:
        lis[i] = lis[i] - 1
 
for i in lis:
    print(i, end=' ')