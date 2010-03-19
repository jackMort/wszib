#!/usr/bin/gnuplot

set term png font "/usr/share/fonts/TTF/ani.ttf" 10
set output "plot.png"
set style data histogram
set style histogram cluster gap 2
set boxwidth .5
set style fill solid .8
set grid
unset xtics

plot "output/awk.time" title "awk",\
	 "output/java.time" title "java",\
	 "output/python.time" title "python",\
	 "output/perl.time" title "perl",\
	 "output/php.time" title "php"
