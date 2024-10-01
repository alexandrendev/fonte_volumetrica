reset
set terminal pngcairo enhanced font "Arial,12" size 800,600
set output "fonteVolumetrica.png"
set xlabel "Sorteios"
set ylabel "Ângulo sólido"
set grid
set yrange [0:14]
set xrange [0:120]


valor = 4*pi

set arrow from graph 0, first valor to graph 1, first valor nohead lw 2 lc rgb "blue" dashtype 2
set label sprintf("4π = %.2f", valor) at graph 0.02, first valor offset 1,1 tc rgb "black"

set arrow from 23.9, graph 0 to 23.9, graph 1 nohead lw 2 lc rgb "black" dashtype 2
set label "Abertura" at 23.9, 1 offset 1,1 tc rgb "black"

plot "resulteidos.txt" using 1:(($1/100000000)*(4*pi)):(erro) with yerrorbars title "Erros", \
     "junção.txt" using 2:(($1/100000000)*(4*pi)) with linespoints linewidth 0.9 pointtype 163 linecolor rgb "red" title "Valor do ângulo sólido"

