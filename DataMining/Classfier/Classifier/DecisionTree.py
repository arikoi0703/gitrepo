import math
class DecisionTree():
	def __init__(self, trainSet):
		self.tail = len(trainSet[0]) - 1
		self.size = len(trainSet)
		self.trainSet = trainSet
		self.decision = ''			#value,condition;	like 10,gt;20,le;...
		self.tree = {}
		self.isTreeExist = False	#check if tree exist

	'''
	current key
	left 	key*2,		< tree[key]
	right	key*2 +1, 	>= tree[key]
	'''
	def setTree(self, tSet=[], key=1, attrIdx=0):
		if key in self.tree.keys():
			return True
		if key == 1 and attrIdx == 0 and tSet == []:
			tSet = self.trainSet
		count = [0,0]
		for data in tSet:
			count[int(data[-1])] += 1
		if count[0] == 0 or count[1] == 0 or attrIdx == self.tail:
			self.tree[key] = count.index(max(count))
			return True
		attr = sorted(tSet, key=lambda item: item[attrIdx])
		maxEntropy = 0
		eValue = 0	#the value to get the max entropy
		preValue = -1
		for i in attr:
			value = float(i[attrIdx])
			if value != preValue:
				left  = [0,0]
				right = [0,0]
				for j in attr:
					if float(j[attrIdx]) < value:
						left[int(j[-1])] += 1
					else:
						right[int(j[-1])] += 1
				e = self.getEntropy(count, left, right)
				if e > maxEntropy:
					maxEntropy, eValue = e, value
				preValue = value
		self.tree[key] = eValue
		left = [ d for d in tSet if float(d[attrIdx]) < eValue ]
		right = [ d for d in tSet if float(d[attrIdx]) >= eValue ]
		resL = self.setTree(left, key*2, attrIdx+1)
		resR = self.setTree(right, key*2+1, attrIdx+1)
		return (resL and resR)

	#[group 0, group 1]	
	def getEntropy(self, setOri, setL, setR):
		sumOri = sum(setOri)
		sumL = sum(setL)
		sumR = sum(setR)
		ori = -sum([ (setOri[i]/sumOri)*math.log(setOri[i]/sumOri, 2) for i in range(len(setOri)) ])
		entropyL = -sum([ (setOri[i]/sumOri)*math.log(setOri[i]/sumOri, 2) for i in range(len(setOri)) ])
		entropyR = -sum([ (setOri[i]/sumOri)*math.log(setOri[i]/sumOri, 2) for i in range(len(setOri)) ])
		return ( ori - (sumL/sumOri)*entropyL - (sumR/sumOri)*entropyR )

	def predictTree(self, testSet):
		result = ''
		if len(testSet[0]) != self.tail:
			print('data size error')
			return result
		keySet = self.tree.keys()
		print(self.tree)
		print(keySet)
		for data in testSet:
			key = 1
			for attr in data:
				if key in keySet:
					if float(attr) < self.tree[key]:
						key = key*2
					else:
						key = key*2+1
				else:
					break
			if key in keySet:
				result += str(self.tree[key])
			else:
				result += str(self.tree[int(key/2)])
		return result


