import sys

answer = open('answer', 'r').readline()

total = len(answer)
print('k,error,accuracy')
for i in range(1,10000,2):
	test = open('./knn_result/' + str(i), 'r').readline()
	error = 0 
	for j in range(total):
		if test[j] != answer[j]:
			error += 1
	print(i, error, (total-error)/total*100, sep=',')

