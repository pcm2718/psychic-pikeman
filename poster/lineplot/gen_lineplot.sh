#!/bin/bash

for budget in 1 5 10 25 50 75 100 250 500 750 1000 2500 5000 7500 10000
do
    echo -n "$budget " >> lineplot.dat

    for size in 3 5 7
    do
    	echo -n "`grep "red" testlogs/testlog_${size}_${budget}.dat | wc -w` " >> lineplot.dat
    done

    echo "" >> lineplot.dat
done
