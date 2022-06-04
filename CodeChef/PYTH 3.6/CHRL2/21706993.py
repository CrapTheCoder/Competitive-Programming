s = input()

c = h = e = f = 0

for i in s:
    if i == 'C': c += 1
    if i == 'H' and h < c: h += 1
    if i == 'E' and e < h: e += 1
    if i == 'F' and f < e: f += 1
        
print(f)
