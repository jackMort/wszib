#-*- coding: utf-8 -*-
from sys import stdin
import operator
import re

# slownik slowo => liczba wystapien
data = {}

# wyrazenie regularne określające słowo
pattern = re.compile( "[a-ź]+" )

# czytanie linia po lini i dodwanie słów do słownika
for line in stdin:
	for word in pattern.findall( line.lower() ):
		data[word] = data.get( word, 0 ) + 1

# sortowanie slownika wg ilosci wystapien
data = sorted( data.items(), reverse=True, key=operator.itemgetter( 1 ) )

# wypisanie 20 pierwszych wyników
for i in data[:20]:
	print i[0], i[1]

