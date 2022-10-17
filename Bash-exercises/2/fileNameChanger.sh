#! /bin/bash

mkdir output 
zipName=$1
sudo unzip $zipName -d output
cd output/input
for file in *
do
	regex="720HD-subtitle([0-9]*).txt"
	if [[ $file =~ $regex ]] 
	then
		sudo mv $file "${BASH_REMATCH[1]}.txt"
	fi
done
cd ..
mv input output
zip -r output.zip output
mv output.zip ../
cd ..

sudo rm -r output 
