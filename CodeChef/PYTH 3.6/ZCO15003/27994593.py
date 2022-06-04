n = int(input())
lr = sorted(tuple(map(int, input().split())) for _ in range(n))

i = 0
c = 0

while i < n:
    x = lr[i][1]

    while i < n and lr[i][0] <= x:
        if lr[i][1] < x:
            x = lr[i][1]

        i += 1
        
    c += 1

print(c)
