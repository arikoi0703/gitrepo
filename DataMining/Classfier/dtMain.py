from Classifier import DecisionTree as DT

testFile = open('DataSet/NSL-KDDTest+.txt', 'r')
trainFile = open('DataSet/NSL-KDDTrain+.txt', 'r')
testSet = []
trainSet = []

for line in testFile:
	data = line[:-1:].split(',')	#remove '\n'
	testSet.append(data)

for line in trainFile:
	data = line[:-1:].split(',')
	trainSet.append(data)

dt = DT.DecisionTree(trainSet)
#dt.setDecision()
dt.setTree()
print('end set tree')
result = dt.predictTree(testSet)

outFile = open('result/dt', 'w')
outFile.write(result)
outFile.close()
print(dt.tree)
