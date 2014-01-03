#
# Two ways of generating a 2D heat map from ascii data
#

set term png
set title "AI Win Percentage, Computation Budget vs Board Size"
unset key
set tic scale 0

# Color runs from white to green
#set palette rgbformula 34,34,36
set cbrange [0:100]
set cblabel "Win Percentage"
unset cbtics

set xrange [-0.5:8.5]
set yrange [-0.5:2.5]

set ytics 1
set ytics 1

set view map
splot '-' matrix with image
39 46 56 84 90 98 96 99 98 
48 45 53 62 71 98 100 99 100 
49 43 44 58 56 86 90 99 100 
e
e
