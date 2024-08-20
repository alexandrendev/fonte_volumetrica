reset
set terminal pngcairo enhanced font "Arial,12" size 800,600
set output "fontePontual.png"
set title "Fonte Pontual"
set xlabel "Altura da fonte"
set ylabel "Ângulo sólido parcial estimado"
set grid

valor = 4*pi

set arrow from graph 0, first valor to graph 1, first valor nohead lw 2 lc rgb "blue" dashtype 2
set label sprintf("4π = %.2f", valor) at graph 0.02, first valor offset 1,0.5 tc rgb "black"


plot "junção.txt" u 2:(($1/100000000)*(4*pi)) w l lw 0.9 lc rgb "red" title "Valor do ângulo sólido"
