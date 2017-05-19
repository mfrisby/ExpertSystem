#!/usr/bin/python

import sys
import re
from utils.printColor import *

Rules = []
Query = ""
Facts = {}
StrLeft = ""
StrRight = ""

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

def implies1(rule, fact):
	global StrLeft
	global StrRight
	canSolve = 0#is False had to return False because rule not solved
	StrLeft = rule.left[:]
	StrRight = rule.right[:]
	result = 0#to add in Fact
	canSolve = solve(None)
	if canSolve == -1:
		return False
	elif canSolve == 0:
		solveRight(False)
	elif canSolve == 1:
		solveRight(True)
	return True#IS SOLVED RETURN TRUE

def solveRight1(result):
	myFact = ''
	if len(StrRight) == 1:
		Facts.update({StrRight:result})
	elif len(StrRight) == 2 and "!" in StrRight:
		Facts.update({(StrRight.replace("!","")):result})
	else:
		print("TODO")

def solveParenthese(s):
	global StrLeft
	if s == None:
		s = StrLeft
	while "(" in s and ")" in s:
		parentheseStart = s.index("(")
		parentheseEnd = s.index(")")
		strParenthese = s[parentheseStart:parentheseEnd+1]
		StrLeft = s.replace(strParenthese, "")
		strParenthese = strParenthese.replace(")","")
		strParenthese = strParenthese.replace("(","")
		print(strParenthese)
		solve(strParenthese)
		print("strleft" + str(StrLeft))
		break
	return 0

def solveAnd(rule):
	s = rule.left
	aV = True
	bV = True
	if s == None:
		print StrLeft
		s = StrLeft
	while "+" in s:
		split = s.split("+")
		if len(split) > 1:
			a = split[0]
			b = split[1]
			if "!" in a:
				aV = False
				a = a.replace("!","")
			if "!" in b:
				bV = False
				b = b.replace("!", "")
			if str(a) in Facts.keys() and str(b) in Facts.keys():
				if Facts[a] == aV and Facts[b] == bV:
					return 1
				else:
					return 0
			else:
				return -1
	return -1

def solveOr(s):
	return 0
def solveXor(s):
	return 0
def solveLeft(s):
	result = 0
	if "(" in StrLeft:
		result = solveParenthese(s)
		s = None
	if "+" in StrLeft:
		result = solveAnd(s)
		s = None
	#if "|" in StrLeft:
		#result = solveOr(s)
	#if "^" in StrLeft:
		#result = solveXor(s)
	return result

def parseRightOrLeft(s):
	parentheses = []
	letters = []
	while "(" in s and ")" in s:
		start = s.index("(")
		end = s.index(")") + 1
		parenthese = s[start:end]
		parentheses.append(parenthese)
		s = s.replace(parenthese, "")
	for i, letter in enumerate(s):
		if i != 0 and s[i -1] == "!":
			continue
		if letter == "!" and i != len(s):
			letters.append(s[i] + s[i + 1])
		else:
			letters.append(letter)
	return parentheses + letters

def implies(rule):
	listFactsRight = []
	resultLeft = -1

	listRulesLeft = parseRightOrLeft(rule.left)
	listFactsRight = parseRightOrLeft(rule.right)
	print("leftStart : " + rule.left + " list : " + str(listRulesLeft))
	print("rightStart : " + rule.right + " list : " + str(listFactsRight))
	resultLeft = solveLeft(listRulesLeft)
	if resultLeft == -1:
		return False
	
	return True

#seems OK
def solveRule():
	while True:
		listPointeur = []
		for rule in Rules:
			listPointeur.append(rule.alreadySolve)
			if rule.alreadySolve == True:
				continue
			for fact in Facts:
				if fact not in rule.left and fact not in rule.right:
					continue
				if rule._get_middle() == "=>":
					rule.alreadySolve = implies(rule)
					break
				elif rule._get_middle() == "<=>":
					rule.alreadySolve = True
					#rule.alreadySolve = ifAndOnlyIf(rule)
					break
		if False not in listPointeur:
			break
	
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
		print "no correct input"
		return
	s = str(sys.argv[1])
	f = open(s, 'r')
	parseFile(f)
	solveRule()
	f.close()
	return
main()