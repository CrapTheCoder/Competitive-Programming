n = int(input())
s = input().strip()

v, h = s.count('V'), s.count('H')

if v == h:
    print('Friendship')
if v < h:
    print('Harshit')
if v > h:
    print('Virat')
