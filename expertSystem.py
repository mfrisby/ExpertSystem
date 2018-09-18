#!/usr/bin/python

import sys
import re
from termcolor import colored, cprint

Rules = []
Query = ""
Facts = {}

#Parse File	
def removeComment(line):
	index = 0
	if '#' in line:
		index = line.index("#")
		return line[:index]
	return line
	
def parseFile(f):
	global Rules
	global Query
	global Facts
	for line in f:
		if line.startswith('#'):
			continue
		elif line.startswith('?'):
			Query =  removeComment(line)
		elif line.startswith('='):
			facts = removeComment(line)
			for letter in facts:
				if letter.isalpha():
					Facts.update({letter:1})
		elif line:
			Rules.append(removeComment(line))
	print(colored(str(Query), 'yellow'), '\n', colored(str(Facts), 'red'), '\n', colored(str(Rules), 'green'))

#priority
# ( ) 1	
# ! not 2
# + and 3
# | or 4
# ^ xor 5
# => implies 6 
# <=> if only if 7

def main():
	if len(sys.argv) != 2:
		print("Error: input expected.")
		return
	s = str(sys.argv[1])
	try:
		f = open(s, 'r')
	except IOError as e:
		print("I/O error({0}): {1}".format(e.errno, e.strerror))
		exit()
	parseFile(f)
	f.close()
	return

main()