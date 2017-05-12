#!/usr/bin/python

import sys
import re
from utils.printColor import *

# ! not
# + and
# ^ xor
# | or
# ( ) 
# => implies
# <=> if only if

Query = ""
Rules = []
Facts = []#true values are saved here (make append a letter if true)

def parseRule(rule):
	splitted = re.split("(<=>)|(=>)", rule)
	while None in splitted:
		splitted.remove(None)
	print splitted

def isItTrue(rule, fact):
	rule = rule.replace(" ", "")
	print rule
	parseRule(rule)
	#if rule.isalpha() and len(rule) == 1:	

def solveWithInitialsFacts():
	newFacts = []
	for rule in Rules:
		for fact in Facts:
			if fact in rule:
				isItTrue(rule, fact)

def removeComment(line):
	index = 0
	if '#' in line:
		index = line.index("#")
		return line[:index]
	return line

def parseFile(f):
	for line in f:
		if line.startswith('#'):
			continue
		elif line.startswith('?'):
			Query = removeComment(line)
		elif line.startswith('='):
			facts = removeComment(line)
			for letter in facts:
				if letter.isalpha():
					Facts.append(letter)
		else:
			s = removeComment(line)
			Rules.append(s)
	printBlue(Rules)
	printYellow(Query)
	printRed(Facts)

def main():
	if len(sys.argv) != 2:
		print "no correct input"
		return
	s = str(sys.argv[1])
	f = open(s, 'r')
	parseFile(f)
	solveWithInitialsFacts()
	f.close()
	return
main()