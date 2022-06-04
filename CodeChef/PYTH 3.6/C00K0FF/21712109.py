ts = ['cakewalk', 'simple', 'easy']
ds = [['easy-medium', 'medium'], ['medium-hard', 'hard']]

for _ in range(int(input())):
    n = int(input())
    d = []

    for i in range(n):
        d.append(input())
        
    if all(i in d for i in ts) and all(any(i in d for i in j) for j in ds):
        print('Yes')
    else:
        print('No')