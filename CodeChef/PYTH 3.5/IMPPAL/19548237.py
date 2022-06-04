for _ in range(int(input())):
    s, m = map(int, input().split())
    st = input()

    for __ in range(m):
        x = int(input())
        a = input().split()

        for i in range(len(a[:-1])):
            st = st.replace(a[i], a[-1])

    if st == st[::-1]:
    	print('Impersonating')
    else:
    	print('Not Impersonating')