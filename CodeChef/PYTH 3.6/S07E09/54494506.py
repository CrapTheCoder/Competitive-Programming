for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()), reverse=True)

    ind = a.index(a[-1])
    print(ind + n * a[-1])