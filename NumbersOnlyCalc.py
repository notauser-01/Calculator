#NumbersOnlyCalc(ulator):
import string
import sys

from modules import *

allowed_chars = [" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "^", "/", "*", "-", "+", "."]
go = False
count = [0, 0]

while go == False:
	argument = input("Give us a problem without variables:").replace(" ", "")
	argument = argument + " "
	index = len(argument)
	for i in range(index):
		if argument[i] not in allowed_chars:
			print("The allowed characters are:")	
			print(allowed_chars)
			break
		if argument[i] == "(":
			count[0] += 1
		if argument[i] == ")":
			count[1] += 1
		if argument[i] in allowed_chars and i == index-1: 
			if count[0] == count[1]:
				go = True
			else:
				print(f"We can't have {count[0]} open parnethesis '(' and {count[1]} closed parenthesis ')' ")
				print(f"Please try again? ...")
				count = [0, 0]
				go = False
print("We can solve that:")

#separate the numbers, from the symbols and make a list of "stuff"
num = ""
thing  = ""
stuff = []

for i in range(0,index):
	if argument[i] == "":
		continue
	if argument[i] in string.digits or argument[i] == ".":
		num = num + argument[i]
	else:
		if num != "":
			stuff.append(float(num))
			num = ""
		thing = argument[i]
		stuff.append(thing)
stuff.remove(" ")

#find negative numbers:
for i in range(len(stuff)):
	if stuff[i] == "-" and stuff[i+1] == "(":
		stuff[i] = float("-1")
		if i == 0:
			continue
		if type(stuff[i-1]) == float:
			stuff.insert(i, "+")
			continue
	if stuff[i] == "-" and i == 0 \
	or stuff[i] == "-" and type(stuff[i-1]) is str:
		stuff[i] = float(stuff[i] + str(stuff[i+1]))
		del stuff[i+1]
		stuff.append(" ")

#allow for scalar multiplication:
for i in range(len(stuff)):
	if i == 0:
		continue
	if type(stuff[i-1]) == float and stuff[i] == "(" \
	or stuff[i-1] == ")" and stuff[i] == "(" \
	or stuff[i-1] == ")" and type(stuff[i]) == float:
		stuff.insert(i, "*")

#find the parenthesis:
parens = []
for i in range(len(stuff)):
	if stuff[i] == "(": 
		parens.append(("open", i))
	if stuff[i] == ")":
		parens.append(("closed", i ))

#find the first, innermost "chunk" ((this first)((then this))):
while "(" in stuff:
	for i in range(len(parens)):
		if parens[i][0] == "closed":
			chunk = stuff[parens[i-1][1] + 1:parens[i][1]]		
			if len(chunk) != 1:
				thing = Arithmacalc(chunk)
			else: 
				thing = chunk[0]

			del stuff[parens[i-1][1]:parens[i][1] + 1]
			stuff.insert(parens[i-1][1], thing)
			
			parens.clear()
			index = len(stuff)
			for j in range(index):
				if stuff[j] == "(":
					parens.append(("open", j))
				if stuff[j] == ")":
					parens.append(("closed", j))
			break

#lacking (chunks) you we can just solve stuff:
if len(stuff) < 2:
	answer = stuff[0]
else:
	answer = Arithmacalc(stuff)

print(f"{argument} = {answer}")