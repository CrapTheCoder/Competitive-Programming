for _ in range(int(input())):
    n, m = map(int, input().split())
    print('No' if (n * m) % 2 else 'Yes')