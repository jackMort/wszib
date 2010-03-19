#!/bin/bash
TIME="/usr/bin/time -f %e"

for i in `seq 10`;
do
	echo "$i ..."
	for directory in awk java perl php python;
	do
		cd $directory 
		$TIME ./run.sh < ../potop.txt > "../output/$directory.txt" 2>> "../output/$directory.time"
		cd ..
	done
done
