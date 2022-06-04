from string import ascii_uppercase

for _ in range(int(input())):
    n = int(input())
    s = [' '] * (2*n + 1)
    s[n] = '*'

    l, r = n-1, n+1

    for i in range(n):
        s[l] = '('
        s[r] = ')'

        l -= 1
        r += 1

        print(*s, sep='')
