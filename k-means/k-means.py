import math

#split dataset into k parts
k = 3

#read data to data[]
fp = open('iris.data', 'r')
data = []
for lines in fp:
	line = lines.split(',')
	line.pop()
	data.append(line)

#pick random number as first center
#and create empty set
dsize = len(data)
psize = dsize/k
now_center = []
pre_center = []
sets = []
dist = []
for i in range(psize):
	now_center.append(data[i*psize])
	sets.append([])
	dist.append(0)
while pre_center != now_center:
	for i in range(dsize):
		for j in range(4):
			dist[0] = dist[0] + math.pow(data[i][j]-now_center[0][j], 2)
			dist[1] = dist[1] + math.pow(data[i][j]-now_center[1][j], 2)
			dist[2] = dist[2] + math.pow(data[i][j]-now_center[2][j], 2)
		sets[dist.index(min(dist))].append(data[i])
	pre_center = now_center
	for i in range(k):
		for j in range(len(sets[i])):
			#new center calculate
		
