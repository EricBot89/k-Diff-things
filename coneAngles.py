import math
import functools
import os
import time

def wait():
	input("\033[36m""	press  enter to continue""\033[0m")

def lcm(x,y):
	return ((x*y)//math.gcd(x,y))

def multiLcm(*args):
	return functools.reduce(lcm,args)

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
	eaD = getDenoms(ea)
	if len(angleList ) == 1:
		return multiLcm(eaD)[0]
	else:
		return multiLcm(eaD)[1]

def getAnglesInTermsOfK (angleList):
	k = getK(angleList)
	return [[(angleList[i][j]*k)//angleList[i][1] for j in range(3)] for i in range(len(angleList))] 

def listBoxerUpperThingy(orders,mults):
	step1 = [[orders[i] for j in range(mults[i])] for i in range(len(orders))]
	step2 = [ item for sublist in step1 for item in sublist]
	return step2

def getDeficFromTwoPi(angleList):
	k = getK(angleList)
	kAngles = getAnglesInTermsOfK(angleList)
	return [kAngles[i][0]-2*k for i in range(len(angleList))]

def getKdiffZeros(angleList):
	orders = getDeficFromTwoPi(angleList)
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
	mults = abelianMult(angleList)
	return listBoxerUpperThingy(orders, mults)

def genusFinder(angleList):
	return functools.reduce(multiLcm,abelianZeros(angleList))

def inputAngles():
	print("\033[4m","\033[1m",'shapes are lists of angles, and each angle should be a space delimited  list of the form:',"\033[0m")
	print('numerator denominator multiplicity')
	angleList = []
	anglein = []
	wait()
	while  anglein != [0,0,0]:
		os.system('clear')
		print(" "'0,0,0 ends')
		print("\033[4m",'current shape:', angleList,"\033[0m")
		anglestring = input()
		anglein = list(map(int,anglestring.split()))
		if len(anglein) == 3  and anglein[1] != 0 and anglein[2] != 0:
			angleList.append(anglein)
			wait()
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

opts = {}
opts[1] = 'Enter a new  shape'
opts[2] = 'Find Everything'
opts[3] = 'Find K'
opts[4] = 'Return the zeroes of the K differential your list of angles represents'
opts[5] = 'Return the zeroes of the  cannonical K covering which lies above the shape'
opts[6] = 'Find the Genus of the Cover'
opts[7] = 'Read a bunch of shapes from a file and output all k-Coverng info'
opts[8] = 'Print the shape currently in memory'
opts[9] = 'Hi'
opts[0] = 'Quit'
print("\033[4m","\033[1m", 'This is the Cone Angle Calculator',"\033[0m")
time.sleep(1)
print(" ",'Use number keys to select menu options, press any key to continue when needed')
time.sleep(1)
polygonAngles = [[1,1,1]]
while True:
		for entry in opts:
			print("	",entry, opts[entry]) 
		print('--------------------------------------------------------------------------------------------------------------------------------------------------')
		nav = input()
		if int(nav) == 0:
			os.system('clear')
			break
		elif int(nav) == 2:
			os.system('clear')
			print("K=", getK(polygonAngles))
			print("Zeroes of K differential = ", getKdiffZeros(polygonAngles))
			print("Zeroes of the cover = ", abelianZeros(polygonAngles))
			print("Genus of the cover = " , genusFinder(polygonAngles))
			print("\n")
			wait()
			os.system('clear')
		elif int(nav) == 1:
			os.system('clear')
			polygonAngles = inputAngles()
			wait()
			os.system('clear')
		elif int(nav)==3:
			os.system('clear')
			print(getK(polygonAngles))
			wait()
			os.system('clear')
		elif int(nav)==4:
			os.system('clear')
			print(getKdiffZeros(polygonAngles))
			wait()
			os.system('clear')
		elif int(nav)==5:
			os.system('clear')
			print(abelianZeros(polygonAngles))
			wait()
			os.system('clear')	
		elif int(nav)==6:
			os.system('clear')
			print(genusFinder(polygonAngles))
			wait()
			os.system('clear')
		elif int(nav) == 8:
			os.system('clear')
			print(polygonAngles)
			wait()
			os.system('clear')
		elif int(nav) == 9:
			os.system('clear')
			print("\n")
			print('hi')
			print("\n")
			wait()
			os.system('clear')
		else:
			os.system('clear')
			print('what?')
			wait()
			os.system('clear')
