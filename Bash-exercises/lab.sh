#!/bin/bash
diraddr=$(pwd)
echo $diraddr
printer () {
	nextdir=$1
	cd $nextdir
	for file  in *
	do
		if [ -d "$file" ]
		then
			printer $file
		else
			echo "$file"
		fi
	done
	cd ..
}

printer $diraddr

