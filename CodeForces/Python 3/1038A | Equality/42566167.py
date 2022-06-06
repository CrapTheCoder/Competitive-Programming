alps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, k = map(int, input().split())
s = input()

print(min([s.count(i) for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:k]]) * k)