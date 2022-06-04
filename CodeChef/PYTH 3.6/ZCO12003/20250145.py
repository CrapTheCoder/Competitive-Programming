def max_len_between(s, paren_type):
    st = []
    length = 0
    max_length = 0

    op = paren_type[0]
    cp = paren_type[1]

    for c in s:
        if c == op:
            st.append(c)
        elif c == cp:
            st.pop()

        if len(st) == 0:
            if length > max_length:
                max_length = length + 1
            length = 0
        else:
            length += 1

    return max_length

def parser(arr):
    return [{1 : '(', 2 : ')', 3 : '[', 4 : ']'}[c] for c in arr]

n = int(input())
a = list(map(int, input().split()))

br = []
dep = []

ret = 0

for i in range(0, n):
    if (a[i] == 1 or a[i] == 3) and br == []:
        br.append(a[i])
        dep.append(1)
        ret = max(ret, dep[-1])

    elif a[i] == 1 and br[-1] == 3:
        br.append(a[i])
        dep.append(dep[-1] + 1)
        ret = max(ret, dep[-1])

    elif a[i] == 3 and br[-1] == 1:
        br.append(a[i])
        dep.append(dep[-1]+1)
        ret = max(ret, dep[-1])

    elif a[i] == 1 or a[i] == 3:
        br.append(a[i])
        dep.append(dep[-1])
        ret = max(ret, dep[-1])

    elif a[i] == 2 or a[i] == 4:
        br.pop()
        dep.pop()

print(ret, max_len_between(parser(a), '()'), max_len_between(parser(a), '[]'))