from string import ascii_lowercase as alps

for _ in range(int(input())):
    s = input()

    ns = ''

    for i in s:
        cur = alps[(alps.index(i) + 1) % 26]

        if cur in 'aeiou':
            cur = cur.upper()

        print(cur, end='')

    print()