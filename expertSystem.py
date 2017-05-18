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

Rules = {}#false while not solved
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
	for line in f:
		#comment
		if line.startswith('#'):
			continue
		#query
		elif line.startswith('?'):
			Query = removeComment(line)
		#initials fact	
		elif line.startswith('='):
			facts = removeComment(line)
			for letter in facts:
					if letter.isalpha():
						Facts.update({letter:True})
		#rules				
		else:
			s = removeComment(line)
			Rules.update({s:False})
	print "Rules"
	printBlue(Rules)
	print "Query"
	printYellow(Query)
	print "Facts"
	printRed(Facts)

#Parse Rules
def splitRule(rule):
	rule = rule.replace(" ", "")
	splitted = re.split("(<=>)|(=>)", rule)
	while None in splitted:
		splitted.remove(None)
	if len(splitted) != 3:
		return None
	return splitted

#left = splitted[0]
#right = splitted[2]
#middle = splitted[1]
def implies(splitted):
	if len(splitted[2]) > 1:
		s = re.split(".", splitted[2])
		while None in s:
			s.remove(None)
	else:
		s = splitted[2]
	print s
	for i in s:
		print i
		Facts.update({i : False})
	print Facts
	print "implies" + str(splitted)

def check(splitted):
	print "check" + str(splitted)

def solveRule(splitted):
	if splitted[1] == "=>":
		implies(splitted)
	elif splitted[1] == "<=>":
		check(splitted)
	
def solveWithInitialsFacts():
	copyFacts = Facts
	copyRules = Rules
	for rule in copyRules:
		for fact in copyFacts:
			if fact in rule:
				splitted = splitRule(rule)
				solveRule(splitted)

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