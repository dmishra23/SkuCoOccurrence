#! /bin/sh
if [ $# -ne 2 ];then
	echo "USAGE : $0 <INPUT_FILENAME> <SIGMA>"
	exit 1
else
	inputFile=$1
	sigma=$2
	python test.py ${inputFile} ${sigma}
	exit 0
fi
