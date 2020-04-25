iris:	main.py Cluster.py iris.data
	test -d result || mkdir result
	python3 main.py iris.data 4 150 3 20 | tr -d "[] " > ./result/result.csv
