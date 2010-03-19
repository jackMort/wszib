BEGIN {
	FS="[^a-zA-Z]+"
}

{
	for( i = 1; i <= NF; i++ )
		words[tolower($i)]++
}

END {
	headSort = "sort -k2 -n -r | head -n20"
	for( i in words )
		print i, words[i] | headSort
	close( headSort )
}
