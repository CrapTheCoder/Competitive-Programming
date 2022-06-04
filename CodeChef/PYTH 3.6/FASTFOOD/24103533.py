for _ in range(int(input())):
    n = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    prefix = [0]
    suffix = [0] * n

    for i in range(n):
        prefix.append((prefix[-1] if i != 0 else 0) + a[i])
        suffix[-(i+1)] = suffix[-i] + b[-(i+1)]

    suffix.append(0)

    m = -1

    for i in range(n+1):
        m = max(prefix[i] + suffix[i], m)

    print(m)