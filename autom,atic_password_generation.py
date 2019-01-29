# your code goes here
import random
import string
def password(s):
	generate_password="".join([random.choice(string.ascii_lowercase+string.digits)for i in range(s)])
	return generate_password
s=int(input())
print(password(s))
