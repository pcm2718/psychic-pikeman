#!/bin/bash

for size in 3 5 7
do
    for budget in 1 5 10 50 100 500 1000 5000 10000
    do
    	echo -n "`grep "red" testlogs/testlog_${size}_${budget}.dat | wc -w` " >> heatmap.dat
    done

    echo "" >> heatmap.dat
done
