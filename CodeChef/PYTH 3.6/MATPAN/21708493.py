alps = 'abcdefghijklmnopqrstuvwxyz'

for _ in range(int(input())):
    p = list(map(int, input().split()))
    s = sorted(set(input()))

    print(sum([p[i] for i in range(26) if alps[i] not in s]))