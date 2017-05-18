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

Rules = []#get 1 class for each rule
Query = ""
Facts = {}#get fact with true/false value

class Rule:
	alreadySolve = False
	def __init__(self, r):
		self.rule = r.replace(" ", "")
		splitted = re.split("(<=>)|(=>)", self.rule)
		while None in splitted:
			splitted.remove(None)
		if len(splitted) == 3:
			self.middle = splitted[1]
			self.right = list(splitted[2])
			self.left = list(splitted[0])
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
			Rules.append(Rule(removeComment(line)))#remove comment + create class + append to list of rules
	print ("Query")
	printYellow(Query)
	print ("Facts")
	printRed(Facts)

#Parse Rules
def check(rule, fact):
	print("check : " + str(rule.rule) + " : " + str(fact))

def implies(rule, fact):
	print("implies" + str(rule.rule) + " : " + str(fact))

def solveRule():
	for rule in Rules:
		if rule.alreadySolve == True:
			print("Already Solve")
			continue
		for fact in Facts:
			if fact not in rule.left and fact not in rule.right:
				print("Not in Facts")
				continue
			if rule._get_middle() == "=>":
				implies(rule, fact)
			elif rule._get_middle() == "<=>":
				check(rule, fact)

#def solveWithInitialsFacts():
	#copyFacts = Facts.copy()
	#for rule in Rules:
		#for fact in Facts:
			#if fact in rule:
				#splitted = splitRule(rule)
				#solveRule(splitted, copyFacts)
	#print("copyFacts = " + str(copyFacts))
	#Facts = copyFacts.copy()

def main():
	if len(sys.argv) != 2:
		print "no correct input"
		return
	s = str(sys.argv[1])
	f = open(s, 'r')
	parseFile(f)
	solveRule()
	f.close()
	return
main()