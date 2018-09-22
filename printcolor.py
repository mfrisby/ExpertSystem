# -*- coding: utf-8 -*-

Yellow = "\033[93m"
Green = "\033[92m"
Blue = "\033[94m"
Red = "\033[91m"
Purple = "\033[35m"
Cyan = "\033[36m"
EndColor = "\033[0m"

def printGreen(myString):
	print(Green + str(myString) + EndColor, end='\n', flush=True)

def printRed(myString):
	print(Red + str(myString) + EndColor, end='\n', flush=True)
	
def printBlue(myString):
	print(Blue + str(myString) + EndColor, end='\n', flush=True)
	
def printYellow(myString):
	print(Yellow + str(myString) + EndColor, end='\n', flush=True)

def printPurple(myString):
	print(Purple + str(myString) + EndColor, end='\n', flush=True)

def printCyan(myString):
	print(Cyan + str(myString) + EndColor, end='\n', flush=True)