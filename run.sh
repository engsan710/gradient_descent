#!/bin/bash

conda --version
if [ $? -eq 0 ]
then
	echo "Anaconda prereq validated"
else
	echo "Need to install Anaconda"
	exit 1
fi

cd src/producer
python createData.py
