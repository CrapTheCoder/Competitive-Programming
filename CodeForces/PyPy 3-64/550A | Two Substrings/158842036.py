def check(c, d):
    i = s.find(c)
    j = s.find(d, i+2)
    return i != -1 and j != -1
 
s = input()
print('YES' if check('AB', 'BA') or check('BA', 'AB') else 'NO')