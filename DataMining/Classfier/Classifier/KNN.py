#return the result of the test file
from queue import Queue
import threading
import math

class KNN():
	def __init__(self, trainSet=[]):
		self.trainSet = trainSet
		
	def run(self,trainSet=[], testSet=[], k=3, threadNum=0):
		self.k = k
		self.thread = threadNum
		result = ''
		if self.thread == 0:
			for testData in testSet:
				result += self.get_group(testData)
		else:
			threadlist = []
			q_group = Queue()
			part = int(len(testSet)/threadNum)
			#add data serial no. to restore the order after multithread compute 
			for no in range(len(testSet)):
				testSet[no].append(no)
			for i in range(threadNum):
				threadlist.append(threading.Thread( \
								target=self.get_group_t, \
								args=(self.trainSet, testSet[i*part:(i+1)*part], q_group, )
								))
				threadlist[i].start()
			#the len(testSet) may not be divided by threadNum
			#process the remain data here
			for i in range(threadNum*part, len(testSet)):
				seq_no = testSet[i][-1]
				group = get_group(testSet[i][:-1])
				q_group.put([group, seq_no])
			for i in range(threadNum):
				threadlist[i].join()
			result_list = []
			for i in range(q_group.qsize()):
				result_list.append(q_group.get())
			result_list = sorted(result_list, key=lambda item: item[-1])
			for r in result_list:
				result += r[0]
		return result	
	
	def get_group(self, testData):
		k_group = []
		k_dist = []
		dist = 0
		for trainData in self.trainSet:
			dist = compute_distance(testData, trainData)
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
	
	def get_group_t(self, trainSet, testSet, q_group):
		for data in testSet:
			data_no = data[-1]
			testData = data[:-1]
			k_group = []
			k_dist = []
			dist = 0
			for trainData in trainSet:
				dist = compute_distance(testData, trainData)
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
			q_group.put(result)

	def get_k_groups(self, testData=[], k=3):
		k_group = []
		dist = 0
		for trainData in self.trainSet:
			dist = compute_distance(testData, trainData)
			if len(k_group) < k or k == -1:
				k_group.append([dist, trainData[-1]])
			elif dist < max(k_group)[0]:
				idx = k_group.index(max(k_group))
				k_group[idx] = [dist, trainData[-1]]
		k_group = sorted(k_group, key=lambda item:item[0])
		k_group = [ k_group[i][1] for i in range(len(k_group)) ]
		return k_group

def compute_distance(data1, data2):
	dist = 0
	for i,j in zip(data1, data2):
		if i != j:
			dist += math.pow(float(i)-float(j), 2)
	return dist


