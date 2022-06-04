for test in range(int(input())):
 for game in range(int(input())):
  hot,num,wan=map(int, input().split())     
  if num%2==0 or hot==wan:
   print(int(num/2))         
  else:
   print(int(num/2) + 1)