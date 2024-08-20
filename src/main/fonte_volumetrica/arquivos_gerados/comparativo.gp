reset
set terminal pngcairo enhanced font "Arial,12" size 800,600
set output "comparativo.png"
set title "Fonte Pontual x Fonte volumétrica"
set xlabel "Altura da fonte"
set ylabel "Vazão"
set grid
set yrange [0:15]

valor = 4*pi

set arrow from graph 0, first valor to graph 1, first valor nohead lw 2 lc rgb "green" dashtype 2
set label sprintf("4π = %.2f", valor) at graph 0.02, first valor offset 1,1 tc rgb "black"

set arrow from 23.9, graph 0 to 23.9, graph 1 nohead lw 2 lc rgb "black" dashtype 2
set label "Abertura" at 23.9, 1 offset 1,1 tc rgb "black"

plot "pontual/junção.txt" u 2:(($1/10000000)*(4*pi)) w l lw 0.9 ps 0.7 lc rgb "red" title "Fonte Pontual", \
"volumetrica/junção.txt" u 2:(($1/10000000)*(4*pi)) w l lw 0.9 ps 0.7 lc rgb "blue" title "Fonte Volumétrica"
