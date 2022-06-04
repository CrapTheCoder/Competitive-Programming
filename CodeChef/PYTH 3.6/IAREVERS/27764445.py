from string import punctuation

n = int(input())

l = []

for i in range(n):
    l.append(''.join([i for i in input() if i not in punctuation]).split()[::-1])


print(*[' '.join(i) for i in l[::-1]], sep='\n')