#!/bin/bash

for size in 3 5 7
do
    for budget in 1 5 10 50 100 500 1000 5000 10000
    do
    	cat testlogs_2/testlog_${size}_${budget}.dat testlogs_3/testlog_${size}_${budget}.dat >> testlogs/testlog_${size}_${budget}.dat 
    done
done
