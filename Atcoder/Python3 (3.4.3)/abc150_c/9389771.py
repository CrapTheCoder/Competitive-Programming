from itertools import permutations

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

x = list(permutations(list(range(1, n + 1))))

print(abs(x.index(p) - x.index(q)))