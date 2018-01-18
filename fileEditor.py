import os
import pickle

def clr():
	os.system('clear') #you'll need to change  this if you're on windows

def wait():
	input("\033[36mPress  enter to continue""\033[0m")

print('This is a thing for creating and editing files containing lots of  "shapes."')

def inputAngles():
	print("\033[4m","\033[1m",'Shapes are lists of angles, and each angle should be a space delimited  list of the form:',"\033[0m")
	print(' numerator denominator multiplicity')
	angleList = []
	anglein = []
	wait()
	while  anglein != [0,0,0]:
		os.system('clear')
		print(" "'0,0,0 ends')
		print("\033[4m ",'current shape:', angleList,"\033[0m")
		anglestring = input()
		anglein = list(map(int,anglestring.split()))
		if len(anglein) == 3  and anglein[1] != 0 and anglein[2] != 0:
			angleList.append(anglein)
		elif len(anglein) != 3:
			print('this is formatted wrongly')
			wait()
		elif anglein == [0,0,0]:
			return angleList
		elif anglein[1] == 0:
			print('cannot divide by 0')
			wait()
		elif anglein[2] == 0:
			print('multiplicity 0 makes no sense')
			wait()
		else:
			print("you've done something wrong")
			wait()

def pickfile(opt):
	clr()
	print("Filename?")
	NameOfFile = input()
	if opt == 1:
		return open(NameOfFile, "rb")
	elif opt == 2:
		return str(NameOfFile)
	elif opt == 3:
		return open(NameOfFile,"wb")

def instructions():
	clr()
	print('there are no instuctions yet')
	wait()
	
def read():
	WorkingFile = pickfile(1)
	clr()
	init = 0
	while True:
		clr()
		current = WorkingFile.name
		if init == 0:
			shapefile = list(pickle.load(WorkingFile))
			init = 1
		print("\033[4m","\033[1m","What would you like to do?","\033[0m")
		print(' current file:', current)
		print('')
		print(" 1. Check a specific shape")
		print(" 2. Read out the whole file")
		print(" 5. Pick a new file") 
		print(" 0. Main Menu")
		nav = input()
		clr()
		if int(nav) == 1:
			print("shape?")
			line = int(input())
			clr()
			if  line <= (len(shapefile)) and  line > 0:
				print("shape", line, ":")
				print('')
				print(shapefile[line-1])
				wait()
			else:
				print('invalid index')
				wait()
		elif int(nav) == 2:
			clr()
			i=1
			print("indices	|	Shape Data")
			for shapes in shapefile:
				print(" ",i,"	|","	".join(map(str,shapes)))
				i=i+1
			wait()
		elif int(nav)==5:
			clr()
			WorkingFile.close()
			WorkingFile = pickfile(1)
			init = 0
			wait()
		elif int(nav) == 0:
			WorkingFile.close()
			break
		else:
			clear()
			print('what?')
			wait()

def append():	
	WorkingFile = pickfile(2)
	clr()
	wfr = open(WorkingFile, "rb")
	shapefile = list(pickle.load(wfr))
	wfr.close()
	while True:
		clr()
		current = WorkingFile
		print("\033[4m","\033[1m","What would you like to do?","\033[0m")
		print(' current file:', current)
		print('')
		print(" 1. Add some shapes to this file")
		print(" 2. Check file contents")
		print(" 5. pick a new file") 
		print(" 0. Main Menu")
		nav = input()
		clr()
		if int(nav) == 1:
			newlines = []
			while True:
				clr()
				print(' Press 1 to add a new shape, press 2 to commit changes, press 0 to quit without commit')
				print(' Shapes entered:', newlines)
				newnav = input()
				if  int(newnav) == 1:
					clr()
					inshape = inputAngles()
					shapefile.append(inshape)
					newlines.append(inshape)
				elif int(newnav) == 2:
					wfw = open(WorkingFile, "wb")
					pickle.dump(shapefile,wfw)
					wfw.close()  
					break
				elif int(newnav) == 0:
					break
				else:
					clr()
					print('what?')
					wait()
		elif int(nav)==2:
			clr()
			i=1
			print("indices	|	Shape Data")
			for shapes in shapefile:
				print(" ",i,"	|","	".join(map(str,shapes)))
				i=i+1
			wait()
		elif int(nav)==5:
			clr()
			WorkingFile = pickfile(2)
			wait()
		elif int(nav) == 0:
			clr()
			break
		else:
			clear()
			print('what?')
			wait()
	
	
def writeNew():
	WorkingFile = pickfile(3)
	clr()
	while True:
		clr()
		current = WorkingFile.name
		print("\033[4m","\033[1m","What would you like to do?","\033[0m")
		print(' current file:', current)
		print('')
		print(" 1. Write some shapes to this file")
		print(" 5. Create a new file") 
		print(" 0. Main Menu")
		nav = input()
		clr()
		if int(nav) == 1:
			newlines = []
			while True:
				clr()
				print('Write a new shape with 1, commit with 2, cancel with 0')
				print('Shapes entered:', newlines)
				newnav = input()
				clr()
				if  int(newnav)==1:
					inshape = inputAngles()
					newlines.append(inshape)
				elif int(newnav)==2:
					pickle.dump(newlines,WorkingFile)
					break
				elif int(newnav)==0:
					break
				else:
					print('what?')
					wait()
		elif int(nav)==5:
			clr()
			WorkingFile.close()
			WorkingFile = pickfile(1)
			wait()
		elif int(nav) == 0:
			WorkingFile.close()
			break
		else:
			clear()
			print('what?')
			wait()


def mainMenu():
	while True:
		clr()
		print("\033[4m","\033[1m","What would you like to do?","\033[0m")
		print(" 1. Read")
		print(" 2. Append")
		print(" 3. Create new")
		print(" 4. Instructions")
		print(" 0. Quit")
		print('___________________________________________')
		nav = input()
		clr()
		if int(nav) == 1:
			read()
		elif  int(nav) == 2:
			append()
		elif int(nav) == 3:
			writeNew()
		elif int(nav) == 4:
			instructions()
		elif int(nav) == 0:
			return False
		else:
			clear()
			print('what?')
			wait()
x = True
while x == True:
	x = mainMenu()
