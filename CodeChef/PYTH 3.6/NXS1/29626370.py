from string import ascii_lowercase, ascii_uppercase

alpsl = ascii_lowercase
alpsu = ascii_uppercase

for _ in range(int(input())):
    s = input()
    
    ns = ''
    
    for i in s:
        if not i.isalpha():
            ns += i
            continue
        
        if i.islower():
            ns += alpsl[(alpsl.index(i) + 3) % len(alpsl)]
        
        if i.upper():
            ns += alpsu[(alpsu.index(i) + 3) % len(alpsu)]
        
    
    print(ns)