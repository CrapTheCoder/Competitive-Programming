INF = float('inf')

for _ in range(int(input())):
    n = int(input())
    s = list(input())

    ans = 0

    l, r = 0, n - 1
    used = [False] * n

    while l < r:
        if s[l] == s[r]:
            pass

        elif l + 1 < r and s[l + 1] == s[r] and not used[l]:
            s[l], s[l + 1] = s[l + 1], s[l]
            used[l] = used[l + 1] = True

            ans += 1

        elif l < r - 1 and s[l] == s[r - 1] and not used[r]:
            s[r], s[r - 1] = s[r - 1], s[r]
            used[r] = used[r - 1] = True

            ans += 1

        l += 1
        r -= 1

    if s != s[::-1]:
        print('NO')
    else:
        print('YES')
        print(ans)