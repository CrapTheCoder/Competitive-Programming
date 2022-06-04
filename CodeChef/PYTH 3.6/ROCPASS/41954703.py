MOD = 10 ** 9 + 7

for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    s1 = s2 = ''

    for i in s:
        if i in 'aeiou':
            s1 += i
        else:
            s2 += i

    print(''.join(sorted(s1)) + s2)
