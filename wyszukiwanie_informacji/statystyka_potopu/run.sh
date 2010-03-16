#!/bin/bash
for directory in awk java perl php python;
do
	cd $directory 
	echo "::$directory"
	time ./run.sh < ../potop.txt > "../output/$directory.txt"
	echo "------------"
	cd ..
done
