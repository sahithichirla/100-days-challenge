import math
n=int(input())
a=abs(math.sqrt(n))
for i in range(1,a+1):
	if n%1==0:
		print(n,"is not a prime number")
		break
else:
	print(n,"is prime number")