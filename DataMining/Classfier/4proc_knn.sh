#!/bin/bash
i=0
while [ $i !=  4 ]
do
	python3 group_knn.py -1 $i ./part/part$i &
	i=$((i+1))
done


