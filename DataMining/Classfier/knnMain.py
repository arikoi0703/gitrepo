from Classifier import KNNthread
from datetime import datetime
import sys

testFile = 'NSL-KDDTest+.txt'
trainFile = 'NSL-KDDTrain+.txt'
path = 'result/'

try:
	flag = 1
	k = int(sys.argv[flag])
	flag = 2
	thread = int(sys.argv[flag])
except:
	if flag == 1:
		k = int(input('k:'))
	thread = int(input('thread:'))

outFile = 'knn_' + str(k) + '_' + str(thread)
out = open(path+outFile, 'w')
test = open(testFile, 'r').read().split('\n')
train = open(trainFile, 'r').read().split('\n')
testSet = [line.split(',') for line in test if line != '']
trainSet = [line.split(',') for line in train if line != '']

runS = datetime.now()
print(outFile, runS)

knn = KNNthread.KNN(trainSet)
result = knn.run(testSet=testSet, k=k, threadNum=thread)
runE = datetime.now()

out.write(result)

print(outFile, runE)
print(outFile, runE-runS)

