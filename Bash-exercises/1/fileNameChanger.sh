#! /bin/bash

for i in *
do 
	regex="720HD-subtitle([0-9]*).txt"
	if [[ $i =~ $regex ]]; then
		mv $i "${BASH_REMATCH[1]}.txt"
	fi
done
