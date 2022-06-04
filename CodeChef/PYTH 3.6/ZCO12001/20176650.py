n = int(input())
s = ['(' if i == '1' else ')' for i in input().split()]

current_max = 0
maxi = 0
ind1 = 0

current_length = 0
length = 0
ind2 = 0

lens = []
inds = []

for i in range(n):
    if s[i] == '(':
        current_max += 1

        if current_max > maxi:
            maxi = current_max
            ind1 = i + 1

        if current_length == 0:
            ind2 = i + 1

        current_length += 1
        length += 1

    if s[i] == ')':
        if current_max > 0:
            current_max -= 1

        current_length -= 1
        length += 1

    if current_length == 0:
        lens.append(length)
        inds.append(ind2)
        length = 0

m = max(lens)

print(maxi, ind1, m, inds[lens.index(m)])
