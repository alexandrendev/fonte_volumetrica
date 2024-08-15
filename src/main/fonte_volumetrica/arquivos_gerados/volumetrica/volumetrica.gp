reset
set terminal pngcairo enhanced font "Arial,12" size 800,600
set output "fonteVolumetrica.png"
set title "Fonte extensa"
set xlabel "Altura da fonte"
set ylabel "Vazão"
set grid
set yrange [0:15]

valor = 4*pi

set arrow from graph 0, first valor to graph 1, first valor nohead lw 2 lc rgb "blue" dashtype 2
set label sprintf("4π = %.2f", valor) at graph 0.02, first valor offset 1,0.5 tc rgb "black"


plot "junção.txt" u 2:(($1/10000000)*(4*pi)) w lp lw 0.9 pt 5 ps 0.7 lc rgb "red" title "Valor do ângulo sólido"
