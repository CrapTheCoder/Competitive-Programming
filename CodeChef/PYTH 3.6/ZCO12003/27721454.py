def solve(s, op, cl):
    st = []
    le = mle = 0

    for c in s:
        if c == op:
            st.append(c)
        if c == cl:
            st.pop()

        le += 1

        if not st:
            if le > mle:
                mle = le

            le = 0

    return mle


def alt_solve(s):
    pre = []
    dep = []
    ma = 0

    for c in s:
        if (c == '(' or c == '[') and pre == []:
            pre.append(c)
            dep.append(1)

        elif (c == '(' and pre[-1] == '[') or (c == '[' and pre[-1] == '('):
            pre.append(c)
            dep.append(dep[-1] + 1)

        elif c == '(' or c == '[':
            pre.append(c)
            dep.append(dep[-1])

        elif c == ')' or c == ']':
            pre.pop()
            dep.pop()

        if dep:
            ma = max(ma, dep[-1])

    return ma

n = int(input())
x = '()[]'
s = ''.join(x[i - 1] for i in list(map(int, input().split())))

print(alt_solve(s), solve(s, '(', ')'), solve(s, '[', ']'))
