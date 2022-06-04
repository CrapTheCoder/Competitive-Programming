for _ in range(int(input())):
    l = list(map(int, input().split()))

    for i in range(25):
        if set(l[i:i+6]) == {1}:
            print('#coderlifematters')
            break
    else:
        print('#allcodersarefun')