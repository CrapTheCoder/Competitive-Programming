MOD = 10 ** 9 + 7

for _ in range(int(input())):
    s = input().strip()
    b = ''

    for i in s:
        if i in 'aeiou':
            b += '1'
        else:
            b += '0'

    print(int(b, 2) % MOD)