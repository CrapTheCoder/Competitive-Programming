n, a, b = map(int, input().split())

ans = (n // (a + b)) * a

if n % (a + b) < a:
    ans += n % (a + b)
else:
    ans += a

print(ans)
