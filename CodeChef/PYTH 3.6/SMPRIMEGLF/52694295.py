n=int(input())+1
while any(n%i==0for i in range(2,n)):n+=1
print(n)