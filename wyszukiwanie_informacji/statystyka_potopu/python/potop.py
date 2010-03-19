#-*- coding: utf-8 -*-
from sys import stdin
import operator
import re

data = {}

pattern = re.compile( "[a-ź]+" )

for line in stdin:
	for word in pattern.findall( line.lower() ):
		data[word] = data.get( word, 0 ) + 1

data = sorted( data.items(), reverse=True, key=operator.itemgetter( 1 ) )

for i in data[:20]:
	print i[0], i[1]

