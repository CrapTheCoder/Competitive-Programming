for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(sum([i % 2 for i in a]) % 2 + 1 if n > 1 else 1)