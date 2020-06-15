import sys

try:
	part = sys.argv[1]
except:
	part = int( input('part: ') )

f = open('../NSL-KDDTest+.txt', 'r').read().split('\n')

size = int( len(f)/part )

for i in range(part-1):
	out = open('part'+str(i), 'w')
	for j in range(i*size, (i+1)*size):
		out.write(f[j]+'\n')
	out.close()

out = open('part'+str(part-1), 'w')
for j in range((part-1)*size, len(f)):
	out.write(f[j]+'\n')
out.close()


