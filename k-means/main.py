import Cluster

fp = open('iris.data', 'r')
dataSet = []
for lines in fp:
	line = lines.split(',')
	line.pop()
	dataSet.append(line)

a = Cluster.KMeans(dataSet, 4, 150, 3)
a.run(50)
