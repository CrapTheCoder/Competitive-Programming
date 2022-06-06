t = input()
 
s_ = t.replace('a', '')
s_ = s_[:len(s_) // 2]
r = t[:-len(s_)] or t
 
if t.endswith(s_) and r + r.replace('a', '') == t:
    print(r)
else:
    print(':(')