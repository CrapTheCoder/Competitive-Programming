for _ in range(int(input())):
    n = int(input())
    s = input().split()

    a = [s[-1][::-1]]
    s = s[:-1]
    n -= 1

    for i in range(n // 2):
        a.append(s[i])
        a.append(s[-i-1])

    if n % 2:
        a.append(s[n // 2])

    print(*a)
