for _ in range(int(input())):
    a, b, c = map(int, input().split())
    p, q, r = map(int, input().split())

    diffs = [p - a, q - b, r - c]

    if any(i < 0 for i in diffs):
        print(-1)
        continue

    print(sum(diffs))
