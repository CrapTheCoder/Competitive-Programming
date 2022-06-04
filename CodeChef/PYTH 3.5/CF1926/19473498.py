for _ in range(int(input())):
    n = int(input())
    s = input().split()
    if s.count('1') > s.count('0'): print('PUB-G')
    if s.count('1') < s.count('0'): print('Fortnite')
    if s.count('1') == s.count('0'): print('fifty-fifty')