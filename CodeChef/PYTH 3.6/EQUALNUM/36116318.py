for _ in range(int(input())):
    a, b = input().split()
    print('equal' if a.replace(',', '') == b.replace(',', '') else 'different')