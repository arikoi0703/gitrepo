# CLUSTERING by python3.7

iris.data is from here [iris.data](http://archive.ics.uci.edu/ml/datasets/iris)

## ENVIROMENT
- python 3.7.3
- R version 3.6.3 (2020-02-29)

## INTRODUCTION
implement k-means in two modes:
- random assign
- assign by definer

default run 30 times each mode
input: filename, dimension, size, cluster number, iterator
output: sse/run ( at the end output all once )

run R script to plot the graph each mode, out, x-axis = iterator, y-axis = sse
output iris_random_assign.jpeg and iris_with_definer.jpeg

Cluser.py
```
import Cluster.py
km = Cluster.KMeans(dataSet, dimension, size, num_cluster)
definerSet = [ [a,b,c], [d,e,f], ... ]  
//in Cluster, this will decide the first cluster
//calculate the weight by the interval[a,b]
//w = 0, x < a
//w = 1, a < x < b
//w = 2, b < x < c, ...

#if not set definer set, the initial cluster will be assign randomly 
km.run(iterator)
km.run(iterator, definerSet)

#to get the sse and cluster result after run
sse = km.get_sse()  
cluster = km.get_cluster()
```

run directly
```shell
$make iris 
//default run, cluster_num=3, iterator=20

$python3 main.py filename dimension size cluster_num iteraror

$rscript rPlot.rs 
//plot graph
```
