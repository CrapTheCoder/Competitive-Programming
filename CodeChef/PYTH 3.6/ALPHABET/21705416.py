s = set(input())

for _ in range(int(input())):
    r = set(input())

    print('Yes' if r.issubset(s) else 'No')
