MOD = 10 ** 9 + 7
 
for _ in range(int(input())):
    k, n = map(int, input().split())
    x = bin(n)[2:][::-1]
 
    s = 0
    for i in range(len(x)):
        if x[i] == '1':
            s = (s + pow(k, i, MOD)) % MOD
 
    print(s)