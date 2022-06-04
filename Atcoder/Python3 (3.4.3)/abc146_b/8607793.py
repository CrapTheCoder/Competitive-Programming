chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n = int(input())
s = input()

print(''.join(chars[(chars.index(i) + n) % 26] for i in s))
