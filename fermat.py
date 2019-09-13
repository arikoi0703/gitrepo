import math

def isSquare(num):
	root = math.sqrt(num)
	if root.is_integer():
		return root
	return False

def is_prime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	r = int(n**0.5)
	f = 5
	while f <= r:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True   

N = input('N = ')
for a in range (int(math.sqrt(N)+1), N):
	b = math.pow(a,2) - N
	b_root = isSquare(b)
	if b_root:
		print(a,b_root,a+b_root, a-b_root)
		print((a+b_root)*(a-b_root))
		print(is_prime(a+b_root), is_prime(a-b_root))
		exit()
