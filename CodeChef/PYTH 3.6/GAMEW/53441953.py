for _ in range(int(input())):
    n = int(input())
    s = input()

    l = [s[0]]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            l.append(s[i])

    dp = [True, False]
    for i in range(2, len(l) + 5):
        dp.append((not dp[i-1]) or (not dp[i-2]))

    print('SAHID' if dp[len(l) - 1] else 'RAMADHIR')
