#!/bin/bash
i=0
while [ $i !=  4 ]
do
	python3 knnMain.py 40$i 0 ./part/part$i &
	i=$((i+1))
done


