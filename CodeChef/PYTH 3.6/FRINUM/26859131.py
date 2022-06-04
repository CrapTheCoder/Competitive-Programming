for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    if not n % 2:
        print(-1)
        continue

    for i in l:
        if l.count(i) == 1:
            print(i)
            break
