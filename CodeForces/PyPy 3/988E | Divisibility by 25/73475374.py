s=input()[::-1]
t=len(s)
g=lambda c,i=0:s.find(str(c), i)+1or 50
i,f=g(0),g(5)
j=min(g(0,i),f)
m=i+j+(j<i)
j=min(g(2),g(7))
l=f+j+(j<f)
if f==t:
 while s[f-2]=='0':f-=1
 l+=t-f
m=min(m,l)
print((-1,m-3)[m<40])