#!/bin/bash

mkdir -p testlogs

for size in 3 5 7
do
    for budget in 1 5 10 25 50 75 100 250 500 750 1000 2500 5000 7500 10000
    do
        for i in {0..99}
        do
            python ../../src/test.py ${size} ${budget} >> testdat/testlog_${size}_${budget}.dat &
        done
    done
done
