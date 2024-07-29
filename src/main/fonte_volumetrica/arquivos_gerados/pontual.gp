reset
set terminal pngcairo enhanced font "Arial,12" size 800,600
set output "fontePontual.png"
set title "Vazão x Altura"
set xlabel "Altura da fonte"
set ylabel "Vazão"
set grid

plot "DATA_PONTUAL.txt" u 2:1 w lp lw 0.9 pt 5 ps 0.7 lc rgb "red" title "vazão em função da altura", \
"" u 2:(1000 - $1) w lp lw 0.9 pt 5 ps 0.7 lc rgb "blue" title "emissões que permaneceram na câmara"