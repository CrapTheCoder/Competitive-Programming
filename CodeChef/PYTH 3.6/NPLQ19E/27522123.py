MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n = int(input())
    
    if n == 0:
        print(0, 0)
    else:
        x = pow(2, n-1, MOD)
        print(x-1, x)
