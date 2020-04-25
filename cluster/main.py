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

#run 30 times
#begin by random assign
sse_km = []
km = Cluster.KMeans(dataSet, dimension, size, num_cluster) 
for i in range(run_times):
	km.run(iterator)
	sse_km.append( km.get_sse() )

#begin by clustering with definer
#define an interval [a, b, c, ...]
# x < a : x = 0, 
# a < x < b : x = 1, ...
definerSet = [[5, 6],[2.8, 3.5],[2, 5],[1, 1.5]]
sse_definer = []
km_definer = Cluster.KMeans(dataSet, dimension, size, num_cluster)
for i in range(run_times):
	km_definer.run(iterator, definerSet)
	sse_definer.append( km_definer.get_sse() ) 

for i in range(run_times):
	print(sse_km[i])

for i in range(run_times):
	print(sse_definer[i])

