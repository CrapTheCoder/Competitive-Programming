for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    while a and a[-1] == 0:
        a.pop()

    print(len(a) - 1)