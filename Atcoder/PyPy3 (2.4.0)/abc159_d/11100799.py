from collections import Counter

n = int(input())
a = list(map(int, input().split()))

d = Counter(a)

ans = 0

for i, c in d.items():
    ans += d[i] * (d[i] - 1) // 2

for i in a:
    ans_ = ans
    ans_ -= d[i] * (d[i] - 1) // 2
    ans_ += (d[i] - 1) * (d[i] - 2) // 2

    print(ans_)