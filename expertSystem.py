#!/usr/bin/python

import sys
import re
from printColor import *

def removeComment(line):
	index = 0
	if '#' in line:
		index = line.index("#")
		return line[:index]
	return line

def parse(f):
	Query = ""
	Rules = []
	for line in f:
		if line.startswith('#'):
			continue
		elif line.startswith('?'):
			Query = removeComment(line)
		else:
			s = removeComment(line)
			Rules.append(s)
	printBlue(Rules)
	printYellow(Query)

def main():
	if len(sys.argv) != 2:
		print "no correct input"
		return
	s = str(sys.argv[1])
	
	f = open(s, 'r')
	parse(f)
	f.close()
	return
main()