#!/usr/bin/python

import sys
import re
from utils.printColor import *

Rules = []
Query = ""
Facts = {}

class Rule:
	alreadySolve = False
	leftResult = False
	rightResult = False
	def __init__(self, r):
		self.rule = r.replace(" ", "")
		splitted = re.split("(<=>)|(=>)", self.rule)
		while None in splitted:
			splitted.remove(None)
		if len(splitted) == 3:
			self.middle = splitted[1]
			self.right = splitted[2]
			self.left = splitted[0]
		printBlue("Rule : " + str(self.rule))
	
	def _get_left(self):
		return self.left
	def _get_right(self):
		return self.right
	def _get_rule_string(self):
		return self.rule
	def _get_middle(self):
		return self.middle

#Parse File	
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
					Facts.update({letter:True})
		else:
			Rules.append(Rule(removeComment(line)))
	printYellow("Query : " + str(Query))
	printRed("Facts : " + str(Facts))

	
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
		print "Error: input expected."
		return
	s = str(sys.argv[1])
	try:
		f = open(s, 'r')
	except IOError as e:
		print "I/O error({0}): {1}".format(e.errno, e.strerror)
		exit()
	parseFile(f)
	f.close()
	return

main()