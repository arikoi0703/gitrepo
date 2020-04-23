import sys
import Cluster

#sys.argv to access the args from command line
#file name, dimension, size, cluster num, iterator

if len(sys.argv) < 6:
	print('input argument as below:')
	print('fileName, dimension, size, cluster number, iterator')

fileName = sys.argv[1]
dimension = int(sys.argv[2])
size = int(sys.argv[3])
num_cluster = int(sys.argv[4])
iterator = int(sys.argv[5])
dataSet = []
fp = open(fileName, 'r')

'''
#for abalone data preprocess
for lines in fp:
	line = lines.split(',')
	if line[0] == 'M':
		line[0] = 0
	elif line[0] == 'F':
		line[0] = 1
	else:
		line[0] = 2
	dataSet.append(line)
'''
#iris data preprocess
for lines in fp:
	line = lines.split(',')
	line.pop()
	dataSet.append(line)

#run times ?
km = Cluster.KMeans(dataSet, dimension, size, num_cluster) 
km.run(iterator)


