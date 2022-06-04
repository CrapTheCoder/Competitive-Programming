for _ in range(int(input())):
    n, k = map(int, input().split())
 
    if n == 1:
        print(0)
        continue
 
    x = max(0, len(bin(k)) - 5)
    while 2 ** x <= k:
        x += 1
 
    x -= 1
 
    print(x + 1 + -(-(n - 2 ** (x+1)) // k))