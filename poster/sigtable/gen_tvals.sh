#!/bin/bash

for size in 3 5 7
do
    for budget in 1 5 10 25 50 75 100 250 500 750 1000 2500 5000 7500 10000
    do
	echo "Size: $size, Budget $budget:" >> siginfo.dat
	python t_val.py $(grep "red" ../tests/testdat/testlog_${size}_${budget}.dat | wc -w) >> siginfo.dat
    done

    echo "" >> siginfo.dat
done
