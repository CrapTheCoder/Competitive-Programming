from sys import stdin
input = stdin.readline
 
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = set(map(int, input().split()))
    k += 1
 
    m = 0
    last = 0
 
    for i in range(100):
        if i in a:
            last = i
 
        if k - 9 * (10 ** (i - last)) > 0:
            m += 9 * 10 ** i
            k -= 9 * (10 ** (i - last))
 
        else:
            m += k * (10 ** last)
            k //= 10
            break
 
    print(m)