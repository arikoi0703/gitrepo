import math
import random

print 'get two prime numbers p, q'
print 'N = pq, r = (p-1)(q-1)'

def gcd(a, b):
	while b != 0:
		r = a % b
		a = b
		b = r
	return a

def coprime(r):
	while True:
		e = random.randint(1, r-1)
		if gcd(e, r) == 1:
			return e

def inverse_modular(e, r):
	d = 1
	while (e*d)%r != 1:
		d = d+1
	return d

p = input('p = ')
q = input('q = ')
N = p*q
r = (p-1)*(q-1)
e = coprime(r)
d = inverse_modular(e, r)
print 'p, q, N, r, e, d'
print p, q, N, r, e, d

p = input('plain text = ')
c = math.pow(p, e) % N
print c
p_ = math.pow(c, d) % N
print p_
