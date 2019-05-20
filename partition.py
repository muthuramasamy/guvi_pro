c=0
k,a,b=map(int,input().split())
for i in range(0,k):
	if (a*i + b*i) == k:
		c=1
if c==1:
	print("YES")
else:
	print("NO")
	
