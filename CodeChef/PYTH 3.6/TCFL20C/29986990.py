MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n = input().strip()

    f = 1

    for i in n:
        i = int(i)

        if i == 7 or i == 9:
            f *= 4
        else:
            f *= 3
        
        f %= MOD

    print(f)
