n=int(input())
m=map(int, input().split())
w=map(int, input().split())
m=list(m)
w=list(w)
a,t,at=[1000001], [1000001], [1000001]
for x in range(n):
 if w[x] == 1:
  a.append(m[x])
 if w[x] == 2:
  t.append(m[x])
 if w[x] == 3:
  at.append(m[x])
if len(a) > 0 and len(t) > 0 and len(at) > 0:
 am = min(a)
 tm = min(t)
 atm = min(at)
 if (am + tm) <= atm:
  print(am + tm)
 else:
  print(atm)

