a, b, c, d = map(int, input().split())

f = b - c
ans = [0]

for x in range(1, b+1):
asd = ans[-1]

asd -= max(0, f)
asd += min(d - c + 1, x)

f = min(f+1, min(d - c + 1, x))

ans.append(asd)

print(sum(ans[a:]))