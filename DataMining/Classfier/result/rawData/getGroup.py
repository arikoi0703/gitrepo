import sys

try:
	k = int(sys.argv[1])
except:
	k = 3

try:
	fileName = [sys.argv[2]]
except:
	fileName = ['part_0', 'part_1', 'part_2', 'part_3']

result = ''
line = 0
for fn in fileName:
	groupSet = open(fn, 'r')
	for group in groupSet:
		line += 1
		counter = {'0':0, '1':0}
		for i in range(k):
			counter[group[i]] += 1
		if counter['0'] > counter['1']:
			result += '0'
		else:
			result += '1'
	groupSet.close()

print(result)




