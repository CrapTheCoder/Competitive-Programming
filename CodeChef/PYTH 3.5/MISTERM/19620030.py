for _ in range(int(input())):
    n = int(input())
    a = {i for i in range(1, n + 1)}
    b = set(map(int, input().split()))

    print(' '.join(str(i) for i in list((a - b))))