# make some data into LaTex Notation
import math
import functools
import os
import pickle
import time

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
	toplist = [[orders[i] for j in range(mults[i])] for i in range(len(orders))]
	return [ item for sublist in toplist for item in sublist]

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
	
def getKdiffZerosForLtx(angleList):
	orders = list(map(lambda x: x//2,getDeficFromTwoPi(angleList)))
	mults = getMults(angleList)
	return ordersandmults(orders,mults)

def abelianZerosForLtx(angleList):
	orders = abealianOrders(angleList)
	mults = [abelianMult(angleList)[i]*getMults(angleList)[i] for i in range(len(angleList))]
	return ordersandmults(orders, mults)
	
def ordersandmults(orders,mults):
	return [[orders[i],mults[i]] for i in range(len(orders))]
	
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

def TableMaker(shapefile,namelist):
	header = '\\begin{tabular}{l | c | c| r}' + '\n'  + '\\textbf{Polyheron} & \\textbf{Stratum of k-differential} &  \\textbf{Stratum of Covering} & \\textbf{Genus} \\\ ' + '\n' +'\\hline' +'\n'
	table = header
	i = 1
	while i <= len(shapefile):
		table = table +  namelist[0][i-1] + ' & $' + differentialStrata(shapefile[i-1],'k') + '$ & $'  + differentialStrata(shapefile[i-1],'a') + '$ &' + str(genusFinder(shapefile[i-1])) + ' \\\ ' + '\n'		
		i = i+1
	table = table + str(' \n\end{tabular}')
	outFile = open('LaTexOutput','w')
	outFile.write(table)
	print(table)
\
def pickfile():
	clr()
	print("Filename?")
	NameOfFile = input()
	return open(NameOfFile, "rb")

def readAndEncode():
	WorkingFile = pickfile()
	clr()
	init = 0
	check =0
	try:
		nameFile = str(WorkingFile.name) + 'Names'
		nameList = open(nameFile, 'r')
	except:
		print("no name file found!")
		print("continue without names?   (Y/N)")
		opt = input()
		if opt == 'Y' or 'y':
			try:
				nameList = open(DummyNames, 'r')
			except:
				check = 1
		elif opt == 'N' or 'n"':
			wait()
			return True
		else:
			return False
	while True:
		clr()
		current = WorkingFile.name
		if init == 0:
			shapefile = list(pickle.load(WorkingFile))
			if check == 0:
				namelist = [nameList.readlines(i) for i in range(len(shapefile))]
			else:
				namelist = [["J" + str(i) for i in range(200)],0]
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
				print("shape", line, ":", nameList.realines(line)[0])
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
				print(" ", nameList.realines(i)[0],"	|","	".join(map(str,shapes)))
				i=i+1
			wait()
		elif int(nav) == 3:
			clr()
			TableMaker(shapefile,namelist)
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
