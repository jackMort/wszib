BEGIN {
	# Separatorem Pól jest wszystko co nie jest wyrazem
	FS="[^a-zA-Z]+"
}

{
	# dodajemy wszystko do tablicy wyraz -> ilość wystąpień
	for( i = 1; i <= NF; i++ )
		words[tolower($i)]++
}

END {
	# sortujemy numerycznie według drugiej kolumny i wypisujemy 20 pierwszych wierszy
	headSort = "sort -k2 -n -r | head -n20"
	for( i in words )
		print i, words[i] | headSort
	close( headSort )
}
