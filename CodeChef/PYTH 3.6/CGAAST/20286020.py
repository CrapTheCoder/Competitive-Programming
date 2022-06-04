for _ in range(int(input())):
    a = input().strip()
    b = input().strip()

    print('Arjun' if sorted(a) == sorted(b) else 'Amit')