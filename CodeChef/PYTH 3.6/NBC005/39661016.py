MOD = 10 ** 9 + 7

for _ in range(int(input())):
    s = input().strip().lower()
    while not s:
        s = input().strip().lower()
    
    st = (ord(s[0]) - ord('a') + 1) * 100

    d = 0
    for i in s:
        d += st + ord(i) - ord('a')

    print(d % MOD)
