for _ in range(int(input())):
    p = int(input())
    a = set(map(int, input().split()))
    q = int(input())
    b = set(map(int, input().split()))

    print(len(a.intersection(b)))