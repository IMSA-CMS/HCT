#!/bin/bash

array=("" "-do2016" "-do2018" )
arrayBin = ("400,500,700,1100,1900,3500,10000")
csbins = "inc"
uncert = ""

for h in "${array[@]}"
do
    for i in "${array[@]}"
    do
	python CITest/CIAnalysis/runFit.py $i -b $h -cs $csbins -unc $uncert
    done
    python runInterpretation.py -c testLimit -t test --CI -r -p --int -e --submit
done