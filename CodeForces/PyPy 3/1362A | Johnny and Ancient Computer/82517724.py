dp = [0] * 10 ** 5
 
for _ in range(int(input())):
    a, b = map(int, input().split())
 
    x = a
 
    while x % 2 == 0:
        x //= 2
 
    if b % x != 0 or bin(b // x).count('1') != 1:
        print(-1)
        continue
 
    c = 0
    x = a
 
    while (x % 2 == 0) and (b % x != 0 or bin(b // x).count('1') != 1):
        x //= 2
        c += 1
 
    t1 = c // 3 + int((c % 3) != 0)
    c = bin(b // x)[::-1].index('1')
    t2 = c // 3 + int((c % 3) != 0)
 
    print(t1 + t2)