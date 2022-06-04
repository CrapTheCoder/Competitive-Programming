def gcd(x, y):
    while y != 0:
        x, y = y, x % y

    return x

for _ in range(int(input())):
    n = int(input())
    a = sorted(set(map(int, input().split())))
    l, r = map(int, input().split())

    lcm = a[0]
    
    for i in a[1:]:
        lcm = (lcm * i) // gcd(lcm, i)
        
        if lcm > r:
            break

    print((r - l) + 1 - (r // lcm - (l - 1) // lcm))
