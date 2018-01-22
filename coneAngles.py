import math
import functools
import os
import pickle

def clr():
	os.system('clear') #you'll need to change this if you're on windows

def wait():
	print("")
	input("\033[36mPress enter to continue""\033[0m")

def lcm(x,y):
	return ((x*y)//math.gcd(x,y))

def multiLcm(angleList):
	return functools.reduce(lcm,angleList)

def getNums(angleList):
	return [angleList[i][0] for i in range(len(angleList))] 

def getDenoms(angleList):
	return [angleList[i][1] for i in range(len(angleList))]

def getMults(angleList):
	return [angleList[i][2] for i in range(len(angleList))]

def makeAnglesEven(angle):
	if angle[0]%2 == 1:
		return [angle[0]*2,angle[1]*2,angle[2]]
	else:
		return angle

def getEvenAngles(angleList):
	return list(map(makeAnglesEven,angleList))
	
def getK(angleList):
	ea = getEvenAngles(angleList)
	denoms = getDenoms(ea)
	return multiLcm(denoms)
	
def getAnglesInTermsOfK(angleList):
	k = getK(angleList)
	return [[(angleList[i][j]*k)//angleList[i][1] for j in range(0,2)] for i in range(len(angleList))] 

def listBoxerUpperThingy(orders,mults):
	return [[orders[i],mults[i]] for i in range(len(orders))]

def getDeficFromTwoPi(angleList):
	k = getK(angleList)
	kAngles = getAnglesInTermsOfK(angleList)
	return [kAngles[i][0]-2*k for i in range(len(angleList))]

def getKdiffZeros(angleList):
	orders = list(map(lambda x: x//2,getDeficFromTwoPi(angleList)))
	mults = getMults(angleList)
	return listBoxerUpperThingy(orders,mults)

def abealianOrders(angleList):
		ea = getEvenAngles(angleList)
		return [(ea[i][0]-2)//2 for i in range(len(angleList))]

def abelianMult(angleList):
	ea=getEvenAngles(angleList)
	k=getK(angleList)
	return [k//ea[i][1] for i in range(len(ea))]

def abelianZeros(angleList):
	orders = abealianOrders(angleList)
	mults = [abelianMult(angleList)[i]*getMults(angleList)[i] for i in range(len(angleList))]
	return listBoxerUpperThingy(orders, mults)

def genusFinder(angleList):
	orders = abealianOrders(angleList)
	mults1 = abelianMult(angleList)
	mults2 = getMults(angleList)
	subtotal = [mults1[i]*mults2[i]*orders[i] for i in range(len(angleList))]
	return (sum(subtotal)+2)//2

def inputAngles():
	print("\033[4m","\033[1m",'Shapes are lists of angles, and each angle should be a space delimited list',"\033[0m")
	print(' Angle inputs should take the form:'"\033[0m",'numerator denominator multiplicity')
	print("")
	angleList = []
	anglein = []
	wait()
	while  anglein != [0,0,0]:
		clr()
		print(" "'0,0,0 ends')
		print("\033[4m",'current shape:', angleList,"\033[0m")
		anglestring = input()
		anglein = list(map(int,anglestring.split()))
		if len(anglein) == 3  and anglein[1] != 0 and anglein[2] != 0:
			angleList.append(anglein)
		elif len(anglein) != 3:
			print('this is formatted wrongly')
			wait()
		elif anglein == [0,0,0]:
			if len(angleList) == 0:
				anglein = [0,0,1]
				print('add some angles!')
				print("")
				wait()
			else:
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

def pickfile():
	clr()
	print("Filename?")
	NameOfFile = input()
	return open(NameOfFile, "rb")
	
def read():
	WorkingFile = pickfile()
	clr()
	init = 0
	isNames=0
	try:
		nameFile = str(WorkingFile.name) + 'Names'
		namelist = open(nameFile, 'r')
		isNames = 1
	except:
		nameList = [(i+1) for i in range(200)]
		
	while True:
		clr()
		current = WorkingFile.name
		if init == 0:
			shapefile = list(pickle.load(WorkingFile))
			init = 1
		if isNames == 1:
			nameList = [namelist.readlines(i+1) for i in range(len(shapefile))]
		print("\033[4m","\033[1m","What would you like to do?","\033[0m")
		print(' current file:', current)
		print(" 1. Read out the whole file")
		print(" 2. Pick a specific shape by index")
		print(" 3. Get everything for every entry in file")
		print(" 0. Main Menu")
		print("")
		nav = input()
		clr()
		if int(nav) == 2:
			print("shape?")
			line = int(input())
			clr()
			if  line <= (len(shapefile)) and  line > 0:
				print("shape", line, ":", str(nameList[line-1][0]))
				print('')
				print(shapefile[line-1])
				print("")
				Y = input("Use this shape in calc? (1 or Y/N)")
				if Y == 'Y' or '1':
					return shapefile[line-1]
				else:
					clr()
					wait()
			else:
				print('invalid index')
				wait()
		elif int(nav) == 1:
			clr()
			i=1
			print("indices	|	Shape Data")
			for shapes in shapefile:
				print(" ", str(nameList[i-1][0]),"	".join(map(str,shapes)), '\n')
				i=i+1
			wait()
		elif int(nav) == 3:
			AlltheCalcs = list(map(doeverything,shapefile))
			i=1
			for calcs in AlltheCalcs:
				print(" ", str(nameList[i-1][0]),calcs)
				i=i+1
			wait()
		elif int(nav) == 0:
			namelist.close()
			WorkingFile.close()
			return [[1,1,4]]
		else:
			clr()
			print('what?')
			wait()


def doeverything(polygonAngles):
	rundown = "	K=" 
	rundown = rundown + str(getK(polygonAngles)) + '\n'
	rundown = rundown + "	Zeroes of K differential = "
	rundown = rundown + str((getKdiffZeros(polygonAngles))) + '\n'
	rundown = rundown + "	Zeroes of the cover = "
	rundown = rundown + str((abelianZeros(polygonAngles))) + '\n'
	rundown = rundown + "	Genus of the cover = " 
	rundown = rundown + str((genusFinder(polygonAngles))) + '\n' + '\n'
	rundown = rundown + '------------------------------------------------------------'
	rundown = rundown + '\n'
	return rundown
	
clr()
opts = {}
opts[1] = 'Enter a new  shape'
opts[2] = 'Find Everything'
opts[3] = 'Find K'
opts[4] = 'Return the zeroes of the K differential your list of angles represents'
opts[5] = 'Return the zeroes of the  cannonical K covering which lies above the shape'
opts[6] = 'Find the Genus of the Cover'
opts[7] = 'Read shapes from a file, call them by index or batch process them'
opts[8] = 'Print the shape currently in memory'
opts[9] = 'Hi'
opts[0] = 'Quit'
print("\033[4m","\033[1m", 'This is the Cone Angle Calculator',"\033[0m")
print(" ",'Use number keys to select menu options')
polygonAngles = [[1,1,1]]
while True:
		for entry in opts:
			print("	",entry, opts[entry]) 
		print('--------------------------------------------------------------------------------------------------------------------------------------------------')
		nav = input()
		if int(nav) == 0:
			clr()
			break
		elif int(nav) == 2:
			clr()
			print(doeverything(polygonAngles))
			wait()
			clr()
		elif int(nav) == 1:
			clr()
			polygonAngles = inputAngles()
			wait()
			clr()
		elif int(nav)==3:
			clr()
			print(getK(polygonAngles))
			wait()
			clr()
		elif int(nav)==4:
			clr()
			print(getKdiffZeros(polygonAngles))
			wait()
			clr()
		elif int(nav)==5:
			clr()
			print(abelianZeros(polygonAngles))
			wait()
			clr()	
		elif int(nav)==6:
			clr()
			print(genusFinder(polygonAngles))
			wait()
			clr()
		elif int(nav)==7:
			clr()
			polygonAngles = read()
			clr()
		elif int(nav) == 8:
			clr()
			print(polygonAngles)
			wait()
			clr()
		elif int(nav) == 9:
			clr()
			print("\n")
			print('Hi!')
			print("\n")
			time.sleep(2)
			clr()
			print("This program is a a calcualtor.")
			print("")
			print("It takes the angles of some flat surface (e.g. a polyhedron) and spits out")
			print("some info about the cannocnical K covering which lies above your flat surface.")
			print("\n")
			print("This tool might be useful if you want to know somthing about translation")
			print("surfaces generated from polygons with rational angles. It will only work for")
			print("flat surfaces where all the cone angles are rational angles.")
			wait()
			clr()
		else:
			clr()
			print('what?')
			wait()
			clr()
