for _ in range(int(input())):
    n = int(input())

    print('Yes' if len(set(input().split())) == n else 'No')