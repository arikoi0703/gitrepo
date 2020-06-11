#return the result of the test file
from queue import Queue
import threading
import math

class KNN():
	thread = 0
	k = 3
	def __init__(self, trainSet):
		self.trainSet = trainSet

	def run(self, testSet=[], k=3, threadNum=0):
		self.k = k
		self.thread = thread
		result = ''
		if self.thread == 0:
			for testData in testSet:
				result += self.knn_group(testData)
			return result
		else:
			threadlist = []
			q_testSet = Queue()
			q_group = Queue
			for i in range(threadNum):

	def knn_group(self, testData):
		k_group = []
		k_dist = []
		dist = 0
		for trainData in self.trainSet:
			dist = self.compute_distance(testData, trainData)
			if len(k_dist) < self.k:
				k_group.append(trainData[-1])
				k_dist.append(dist)
			elif dist < max(k_dist):
				idx = k_dist.index(max(k_dist))
				k_group[idx] = trainData[-1]
				k_dist[idx] = dist
		counter = [0] * 2	#not a general way
		result = ''
		for i in k_group:
			counter[int(i)] += 1
		result = str(counter.index(max(counter)))
		return result

	def knn_group_t(self, trainSet, q_testSet, q_group):
		while q_testSet.qsize() > 0:
			data = q_testSet.get()
			data_no = data[-1]
			testData = data[:-1]
			k_group = []
			k_dist = []
			dist = 0
			for trainData in trainSet:
				dist = self.compute_distance(testData, trainData)
				if len(k_dist) < self.k:
					k_group.append(trainData[-1])
					k_dist.append(dist)
				elif dist < max(k_dist):
					idx = k_dist.index(max(k_dist))
					k_group[idx] = trainData[-1]
					k_dist[idx] = dist
			counter = [0] * 2	#not a general way
			for i in k_group:
				counter[int(i)] += 1
			result = [str(counter.index(max(counter))), data_no]
			q.put(result)

	def compute_distance(self, testData, trainData):
		dist = 0
		for i,j in zip(testData, trainData):
			dist += math.pow(float(i)-float(j), 2)
		return dist


