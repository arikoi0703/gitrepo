iris:	main.py Cluster.py iris.data
	test -d result || mkdir result
	python3 main.py iris.data 4 150 3 20 | tr -d "[] " > ./result/result.csv

sep_iris:	./result/result.csv
	tail -n 60 ./result/result.csv > ./result/sse.csv
	head -n 60 ./result/result.csv > ./result/init_cluster.csv

clean:
	rm -rf ./result
