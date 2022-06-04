for _ in range(int(input())):
	n, v1, v2 = map(int, input().split())
	
	if(v1 * v1 * 2) > (v2 * v2):
		print('Stairs')
	else:
		print('Elevator')