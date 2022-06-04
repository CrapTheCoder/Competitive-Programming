from collections import Counter

s = input().strip()
c = Counter(s)

if (c['L'] == c['R']) and (c['U'] == c['D']):
    print('true')
else:
    print('false')