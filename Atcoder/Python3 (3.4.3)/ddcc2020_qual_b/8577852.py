x = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

s = input()

if s == 'SUN':
    print(7)
else:
    print(x.index('SUN') - x.index(s))