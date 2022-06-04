n = int(input())
s = input()

while 'RR' in s or 'GG' in s or 'BB' in s:
    s = s.replace('RR', 'R')
    s = s.replace('GG', 'G')
    s = s.replace('BB', 'B')

print(n - len(s))
