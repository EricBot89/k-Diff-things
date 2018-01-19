# make some data into LaTex Notation
import math
import functools
import os
import pickle
import time

def clr():
	os.system('clear') #you'll need to change  this if you're on windows

def wait():
	print("")
	input("\033[36m Press enter to continue""\033[0m")

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
	
def clr():
	os.system('clear') #you'll need to change  this if you're on windows

def wait():
	print("")
	input("\033[36m Press enter to continue""\033[0m")

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

def ordersandmults(orders,mults):
	return [[orders[i],mults[i]] for i in range(len(orders))]

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
	return  (sum(abelianZeros(angleList))) // 2

def getKdiffZerosForLtx(angleList):
	orders = getDeficFromTwoPi(angleList)
	mults = getMults(angleList)
	return ordersandmults(orders,mults)

def abelianZerosForLtx(angleList):
	orders = abealianOrders(angleList)
	mults = abelianMult(angleList)
	return ordersandmults(orders, mults)

def zeroesListBuilder(Zeros):
	i=len(Zeros)
	j=0
	ZeroList = '('
	while j < i:
		bs = str(Zeros[j][0]) 
		ex = '{' + str(Zeros[j][1]) + '}'
		if j > 0 :
			ZeroList = ZeroList +  ','
		ZeroList = ZeroList + str('{}^{}').format(bs,ex)
		j = j+1
	ZeroList = ZeroList + str(')')
	return str(ZeroList)
	
def  differentialStrata(angleList,opt):
	H = '{H}'
	K = str(getK(angleList))
	K = '{' + K + '}'
	begining = str("\\mathcal{}_{}").format(H, K)
	if opt == 'k':
		kd = getKdiffZerosForLtx(angleList)
		kdStrata = begining + zeroesListBuilder(kd)
		return kdStrata
	elif opt == 'a':
		ad = abelianZerosForLtx(angleList)
		adStrata = begining + zeroesListBuilder(ad)
		return adStrata
	else:
		return

def TableMaker(shapefile):
	header = '\\begin{tabular}{l | c | c| r}' + '\n'  + '\\textbf{Polyheron} & \\textbf{Stratum of k-differential} &  \\textbf{Stratum of Covering} & \\textbf{Genus} \\\ ' + '\n' +'\\hline' +'\n'
	table = header
	i = 1
	while i <= len(shapefile):
		table = table +  str(i) + ' &' + differentialStrata(shapefile[i-1],'k') + ' &'  + differentialStrata(shapefile[i-1],'a') + ' &' + str(genusFinder(shapefile[i-1])) + ' \\\ ' + '\n'		
		i = i+1
	table = table + str(' \n\end{tabular}')
#	outFile = open('LaTexOutput','x')
#	outFile.write(table)
	print(table)

def pickfile():
	clr()
	print("Filename?")
	NameOfFile = input()
	return open(NameOfFile, "rb")

def readAndEncode():
	WorkingFile = pickfile()
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
		print(" 1. Read out the whole file")
		print(" 2. Pick a specific shape by index and get LaTeX code for its strata and Genus")
		print(" 3. Convert everything to LaTeX Table")
		print(" 5. Pick a new file") 
		print(" 0. Quit")
		print("")
		nav = input()
		clr()
		if int(nav) == 2:
			print("shape?")
			line = int(input())
			clr()
			if  line <= (len(shapefile)) and  line > 0:
				print("shape", line, ":")
				print('')
				print(shapefile[line-1])
				print("")
				print("k-diff strata:", differentialStrata(shapefile[line-1],'k'))
				print("stratum of the cover:", differentialStrata(shapefile[line-1],'a'))
				print('')
				wait()
			else:
				print('invalid index')
				wait()
		elif int(nav) == 1:
			clr()
			i=1
			print("indices	|	Shape Data")
			for shapes in shapefile:
				print(" ",i,"	|","	".join(map(str,shapes)))
				i=i+1
			wait()
		elif int(nav) == 3:
			clr()
			TableMaker(shapefile)
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
clr()			
print('This program takes an input file of formatted shapes and outputs LaTex Code for all the K differential covering info')
wait()
readAndEncode()
