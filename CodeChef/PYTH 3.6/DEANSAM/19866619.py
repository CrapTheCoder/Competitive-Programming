n = int(input())

arr = list(map(int, input().split()))

m = 10 ** 10
dum = m

for i in range(n):
    if (dum > 0):
        dum = arr[i]
    else:
        dum += arr[i]
    m = min(m, dum)

print(m)