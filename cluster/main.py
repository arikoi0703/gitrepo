import sys
import Cluster

#sys.argv to access the args from command line
#file name, dimension, size, cluster num, iterator

if len(sys.argv) < 6:
	print('input argument as below:')
	print('fileName, dimension, size, cluster number, iterator')
	exit(1)

run_times = 30
fileName = sys.argv[1]
dimension = int(sys.argv[2])
size = int(sys.argv[3])
num_cluster = int(sys.argv[4])
iterator = int(sys.argv[5])
dataSet = []
fp = open(fileName, 'r')

#iris data preprocess
for lines in fp:
	line = lines.split(',')
	line.pop()
	dataSet.append(line)

sse_km = []
#run 30 times
#begin by random assign

km = Cluster.KMeans(dataSet, dimension, size, num_cluster) 
for i in range(run_times):
	sse_km.append( km.run(iterator) )

#begin by clustering with definer
#define an interval [a, b, c, ...]
# x < a : x = 0, 
# a < x < b : x = 1, ...
definerSet = [[5, 6],[3, 3.5],[2, 5],[1, 1.5]]
sse_with_definer = []
km_with_definer = Cluster.KMeans(dataSet, dimension, size, num_cluster)
for i in range(run_times):
	sse_with_definer.append(km_with_definer.run_with_definer(iterator, definerSet)) 


for i in range(run_times):
	print(sse_km[i])

for i in range(run_times):
	print(sse_with_definer[i])

