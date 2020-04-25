# CLUSTERING by python3.7

implement k-means in two modes:
- random assign
- assign by definer

default run 30 times each mode
input: filename, dimension, size, cluster number, iterator
output: sse/run ( at the end output all once )

run R script to plot the graph each mode, out, x-axis = iterator, y-axis = sse
output iris_random_assign.jpeg and iris_with_definer.jpeg

```bash
//default run, cluster_num=3, iterator=20
$make iris
//run
$python3 main.py filename dimension size cluster_num iteraror
//plot graph
$rscript rPlot.rs
```
