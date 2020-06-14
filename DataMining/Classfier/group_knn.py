from Classifier import KNN
from datetime import datetime
import pickle
import sys

testFile = 'DataSet/NSL-KDDTest+.txt'
trainFile = 'DataSet/NSL-KDDTrain+.txt'

path = 'result/'

try:
	flag = 1
	k = int(sys.argv[flag])
	flag = 2
	part_no = int(sys.argv[flag])
	flag = 3
	testFile = sys.argv[flag]
except:
	if flag != 3: 
		if flag == 1:
			k = int(input('k:'))
		part_no = int(input('part_no:'))


outFile = 'knn_group_' + str(k) + '_' + str(part_no)
out = open(path+outFile, 'w')
test = open(testFile, 'r').read().split('\n')
train = open(trainFile, 'r').read().split('\n')
testSet = [line.split(',') for line in test if line != '']
trainSet = [line.split(',') for line in train if line != '']

runS = datetime.now()
print(outFile, runS)

knn = KNN.KNN(trainSet)
result = []

#get the group sorted by distance of every test data
for testData in testSet:
	result = knn.get_k_groups(testData, k)
	out.write(str(result)+'\n')

out.close()

runE = datetime.now()

print(outFile, runE)
print(outFile, runE-runS)

