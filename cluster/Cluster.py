import math
import random

class KMeans():
	def __init__(self, dataSet, dimension, size, num_cluster):
		self.__centroid = [0] * num_cluster
		self.__cluster = [0] * size
		self.__dataSet = dataSet
		self.__dimension = dimension
		self.__size = size
		self.__num_cluster = num_cluster
		self.__sse = []

	def init_run(self):
		self.__sse = []
	
	def run(self, num_iter, definer=[]):
		self.init_run()
		self.init_assign(definer, self.__num_cluster)
		print(self.__cluster)
		#print(self.__cluster)
		self.update()
		self.compute_sse()
		for i in range(1, num_iter):
			self.assign()
			self.update()
			self.compute_sse()
		#print(self.__cluster)

	def get_sse(self):
		return self.__sse
	
	def get_cluster(self):
		return self.__cluster

	def assign(self):		
		for i in range(self.__size):
			temp_cluster = 0
			dist = self.compute_distance(self.__dataSet[i], self.__centroid[0])
			for j in range(1, self.__num_cluster):
				new_dist = self.compute_distance(self.__dataSet[i], self.__centroid[j])
				if new_dist < dist:
					dist = new_dist
					temp_cluster = j
			self.__cluster[i] = temp_cluster
			
	def update(self):
		self.check_empty_set()
		summation = []
		for i in range(self.__num_cluster):
			summation.append([0]*self.__dimension)
		count = [0] * self.__num_cluster
		for i in range(self.__size):
			cluster_no = self.__cluster[i]
			for j in range(self.__dimension):
				summation[ cluster_no ][j] = summation[ cluster_no ][j] + float(self.__dataSet[i][j])
			count[ cluster_no ] = count[ cluster_no ] + 1
		#print('comp_center: ', count)
		for i in range(self.__num_cluster):
			count[i] = 1 if count[i] == 0 else count[i]
			for j in range(self.__dimension):
				summation[i][j] = summation[i][j] / count[i]
			self.__centroid[i] = summation[i]
	
	#random assign if definer is not defined
	#definer = [ [], [], [], ... ]
	#it's good if every definer[] has the same len()
	def init_assign(self, definer=[], definer_cluster=1):
		if definer == []:
			for i in range(self.__size):
				self.__cluster[i] = random.randrange(self.__num_cluster)
		else:
			definer_range = len(definer) * len(definer[0])
			sep = definer_range / definer_cluster
			for i in range(self.__size):
				c = 0
				for j in range(self.__dimension):
					isSet = False
					for k in range(len(definer[j])):
						if float(self.__dataSet[i][j]) < definer[j][k]:
							c = c + k; isSet = (not isSet); break;
					if not isSet:
						c = c + k + 1
				self.__cluster[i] = definer_cluster - 1
				for j in range(definer_cluster):
					if c < (sep + sep*j):
						self.__cluster[i] = j; break;

	def check_empty_set(self):
		count = []
		for i in range(self.__num_cluster):
			count.append(0)
		for i in range(self.__size):
			count[self.__cluster[i]] = count[self.__cluster[i]] + 1
		if min(count) == 0:
			self.__cluster[random.randrange(self.__size)] = count.index(min(count))
	
	#not use, make the num of each cluster more balance
	def balance(self):
		if max(count) > min(count)*2:
			max_cluster = count.index(max(count))
			min_cluster = count.index(min(count))
			for i in range(self.__size):
				if self.__cluster[i] == max_cluster:
					self.__cluster[i] = min_cluster
					count[min_cluster] = count[min_cluster] + 1
					count[max_cluster] = count[max_cluster] - 1
				if count[min_cluster] >= count[max_cluster]:
					break		

	def compute_distance(self, point, center):
		distance = 0
		for i in range(self.__dimension):
			distance = distance + math.pow(float(point[i])-float(center[i]), 2)
		return distance

	def compute_sse(self):
		sse = 0
		for i in range(self.__size):
			sse = sse + self.compute_distance(self.__dataSet[i], self.__centroid[self.__cluster[i]])
		self.__sse.append(sse)
'''		
	def determine_cluster(self, clusterSet):
		size = len(clusterSet)
		match = 0
		if self.__size != size:
			print("set size not match!")
		else:
			for i in range(clusterSet):
				if self.__cluster[i] == 
'''
