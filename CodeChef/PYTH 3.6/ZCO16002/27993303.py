def main():
    inp = list(map(int, input().split()))
    n, a = inp[0], sorted(inp[1:])

    f = a[-1] - a[0]

    dp = [[1] * f for _ in range(n)]

    m = -1

    for i, x in enumerate(a):
        g = -1
        
        for j, y in enumerate(a[:i]):
            h = x - y - 1
            
            dp[i][h] = 1 + dp[j][h]
            
            if dp[i][h] > g:
                g = dp[i][h]

        if g > m:
            m = g

    print(m)

main()
