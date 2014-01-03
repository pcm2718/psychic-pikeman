reset
set terminal png size 720,640
set xlabel "MCTS Budget"
set ylabel "Victory Count"
set xrange [1:10000]
set yrange [0:315]


set title "Victory Count vs MCTS Budget"
set key reverse inside
set logscale x 10
set output 'lineplot.png'
set style data linespoints
plot "lineplot.dat" using 1:2 lt 1 lw 2 title '3x3 Field' , \
     "lineplot.dat" using 1:3 lt 2 lw 2 title '5x5 Field' , \
     "lineplot.dat" using 1:4 lt 3 lw 2 title '7x7 Field' , \
