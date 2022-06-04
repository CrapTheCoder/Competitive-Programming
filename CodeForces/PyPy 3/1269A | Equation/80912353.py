def is_comp(n):
    c = 0
 
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            c += 1
 
            if n // i != i:
                c += 1
 
    return c
 
n = int(input())
 
i = n+1
 
while True:
    if 2 < is_comp(i) and 2 < is_comp(i-n):
        print(i, i-n)
        break
 
    i += 1