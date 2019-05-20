# your code goes here

n,a,b=map(int,input().split())
if n%2==0:
	if a+b<n:
		print("YES")
	elif a+b==n:
		print("YES")
	elif a%2==0 and b%2==0:
		print("NO")
	else:
		print("NO")
else:
	if a+b<n:
		print("NO")
	elif a+b==n:
		print("YES")
	else:
		print("NO")
