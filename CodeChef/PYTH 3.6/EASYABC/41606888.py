s = input()

maxi = -1

if 'a' in s:
    if 'b' in s: maxi = max(maxi, abs(s.index('a') - s.rindex('b')), abs(s.rindex('a') - s.index('b')))
    if 'c' in s: maxi = max(maxi, abs(s.index('a') - s.rindex('c')), abs(s.rindex('a') - s.index('c')))

if 'b' in s:
    if 'a' in s: maxi = max(maxi, abs(s.index('b') - s.rindex('a')), abs(s.rindex('b') - s.index('a')))
    if 'c' in s: maxi = max(maxi, abs(s.index('b') - s.rindex('c')), abs(s.rindex('b') - s.index('c')))

if 'c' in s:
    if 'a' in s: maxi = max(maxi, abs(s.index('c') - s.rindex('a')), abs(s.rindex('c') - s.index('a')))
    if 'b' in s: maxi = max(maxi, abs(s.index('c') - s.rindex('b')), abs(s.rindex('c') - s.index('b')))

print(maxi)