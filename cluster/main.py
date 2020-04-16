import sys
import Cluster

#sys.argv to access the args from command line
#file name, dimension, size, cluster num, iterator

if len(sys.argv) < 6:
	print('input argument as below:')
	print('fileName, dimension, size, cluster numberm, iterator')

fileName = sys.argv[1]
dimension = int(sys.argv[2])
size = int(sys.argv[3])
num_cluster = int(sys.argv[4])
iterator = int(sys.argv[5])
dataSet = []
fp = open(fileName, 'r')

for lines in fp:
	line = lines.split(',')
	line.pop()
	dataSet.append(line)

a = Cluster.KMeans(dataSet, dimension, size, num_cluster)
a.run(iterator)
