#!/bin/bash

k=3
args=("$@")
for ((i=0; i<$#; i++))
do
	if [ ${args[$i]} == "-k" ]; then
		((i++))
		if [[ ${args[$i]} =~ $re_num ]]; then
			k=${args[$i]}
		fi
	fi	
done

python3 rawData/getGroup.py $k rawData/part_0 | tr -d '\n' > $k
python3 rawData/getGroup.py $k rawData/part_1 | tr -d '\n' >> $k
python3 rawData/getGroup.py $k rawData/part_2 | tr -d '\n' >> $k
python3 rawData/getGroup.py $k rawData/part_3 | tr -d '\n' >> $k 

