l=open("WheatWholeGenomeLength.txt","r")

noOfLines=0
freqACGT=[] #loc
freqCCGA=[] #locCCGA
freqCCGAC=[]	#locCCGAC

lengthsOfLines=[]

for x in range(31):
	freqCCGAC.append(0)
	freqCCGA.append(0)
	freqACGT.append(0)

for line in l:
	noOfLines+=1
	lengthsOfLines.append(len(line))
	line.upper
	ACGT=[]
	CCGAC=[]
	CCGA=[]
	for n in xrange (len(line)-4):
		if (line[n:n+4]=="ACGT" ):
			ACGT.append(n)
		if (line[n:n+4]=="CCGA" ):
			CCGA.append(n)
		if (line[n:n+5]=="CCGAC" ):
			CCGAC.append(n)
	for i in range (len(ACGT)-1):
		for j in range(1-8):
			if(i+j>=len(ACGT)): break
			if((ACGT[i+j] - ACGT[i]-4)>30): break
			if((ACGT[i+j] - ACGT[i]-4)==0):
				freqACGT[0]+=1
			if((ACGT[i+j] - ACGT[i]-4)==1):
				freqACGT[1]+=1
			if((ACGT[i+j] - ACGT[i]-4)==2):
				freqACGT[2]+=1
			if((ACGT[i+j] - ACGT[i]-4)==3):
				freqACGT[3]+=1
			if((ACGT[i+j] - ACGT[i]-4)==4):
				freqACGT[4]+=1
			if((ACGT[i+j] - ACGT[i]-4)==5):
				freqACGT[5]+=1
			if((ACGT[i+j] - ACGT[i]-4)==6):
				freqACGT[6]+=1
			if((ACGT[i+j] - ACGT[i]-4)==7):
				freqACGT[7]+=1
			if((ACGT[i+j] - ACGT[i]-4)==8):
				freqACGT[8]+=1
			if((ACGT[i+j] - ACGT[i]-4)==9):
				freqACGT[9]+=1
			if((ACGT[i+j] - ACGT[i]-4)==10):
				freqACGT[10]+=1
			if((ACGT[i+j] - ACGT[i]-4)==11):
				freqACGT[11]+=1
			if((ACGT[i+j] - ACGT[i]-4)==12):
				freqACGT[12]+=1
			if((ACGT[i+j] - ACGT[i]-4)==13):
				freqACGT[13]+=1
			if((ACGT[i+j] - ACGT[i]-4)==14):
				freqACGT[14]+=1
			if((ACGT[i+j] - ACGT[i]-4)==15):
				freqACGT[15]+=1
			if((ACGT[i+j] - ACGT[i]-4)==16):
				freqACGT[16]+=1
			if((ACGT[i+j] - ACGT[i]-4)==17):
				freqACGT[17]+=1
			if((ACGT[i+j] - ACGT[i]-4)==18):
				freqACGT[18]+=1
			if((ACGT[i+j] - ACGT[i]-4)==19):
				freqACGT[19]+=1
			if((ACGT[i+j] - ACGT[i]-4)==20):
				freqACGT[20]+=1
			if((ACGT[i+j] - ACGT[i]-4)==21):
				freqACGT[21]+=1
			if((ACGT[i+j] - ACGT[i]-4)==22):
				freqACGT[22]+=1
			if((ACGT[i+j] - ACGT[i]-4)==23):
				freqACGT[23]+=1
			if((ACGT[i+j] - ACGT[i]-4)==24):
				freqACGT[24]+=1
			if((ACGT[i+j] - ACGT[i]-4)==25):
				freqACGT[25]+=1
			if((ACGT[i+j] - ACGT[i]-4)==26):
				freqACGT[26]+=1
			if((ACGT[i+j] - ACGT[i]-4)==27):
				freqACGT[27]+=1
			if((ACGT[i+j] - ACGT[i]-4)==28):
				freqACGT[28]+=1
			if((ACGT[i+j] - ACGT[i]-4)==29):
				freqACGT[29]+=1
			if((ACGT[i+j] - ACGT[i]-4)==30):
				freqACGT[30]+=1
"""			
	for i in range (len(CCGA)-1):
		for j in range(1-8):
			if(i+j>=len(ACGT)): break
			if((CCGA[i+j] - CCGA[i]-4)>30): break
			if((CCGA[i+j] - CCGA[i]-4)==0):
				freqCCGA[0]+=1
			if((CCGA[i+j] - CCGA[i]-4)==1):
				freqCCGA[1]+=1
			if((CCGA[i+j] - CCGA[i]-4)==2):
				freqCCGA[2]+=1
			if((CCGA[i+j] - CCGA[i]-4)==3):
				freqCCGA[3]+=1
			if((CCGA[i+j] - CCGA[i]-4)==4):
				freqCCGA[4]+=1
			if((CCGA[i+j] - CCGA[i]-4)==5):
				freqCCGA[5]+=1
			if((CCGA[i+j] - CCGA[i]-4)==6):
				freqCCGA[6]+=1
			if((CCGA[i+j] - CCGA[i]-4)==7):
				freqCCGA[7]+=1
			if((CCGA[i+j] - CCGA[i]-4)==8):
				freqCCGA[8]+=1
			if((CCGA[i+j] - CCGA[i]-4)==9):
				freqCCGA[9]+=1
			if((CCGA[i+j] - CCGA[i]-4)==10):
				freqCCGA[10]+=1
			if((CCGA[i+j] - CCGA[i]-4)==11):
				freqCCGA[11]+=1
			if((CCGA[i+j] - CCGA[i]-4)==12):
				freqCCGA[12]+=1
			if((CCGA[i+j] - CCGA[i]-4)==13):
				freqCCGA[13]+=1
			if((CCGA[i+j] - CCGA[i]-4)==14):
				freqCCGA[14]+=1
			if((CCGA[i+j] - CCGA[i]-4)==15):
				freqCCGA[15]+=1
			if((CCGA[i+j] - CCGA[i]-4)==16):
				freqCCGA[16]+=1
			if((CCGA[i+j] - CCGA[i]-4)==17):
				freqCCGA[17]+=1
			if((CCGA[i+j] - CCGA[i]-4)==18):
				freqCCGA[18]+=1
			if((CCGA[i+j] - CCGA[i]-4)==19):
				freqCCGA[19]+=1
			if((CCGA[i+j] - CCGA[i]-4)==20):
				freqCCGA[20]+=1
			if((CCGA[i+j] - CCGA[i]-4)==21):
				freqCCGA[21]+=1
			if((CCGA[i+j] - CCGA[i]-4)==22):
				freqCCGA[22]+=1
			if((CCGA[i+j] - CCGA[i]-4)==23):
				freqCCGA[23]+=1
			if((CCGA[i+j] - CCGA[i]-4)==24):
				freqCCGA[24]+=1
			if((CCGA[i+j] - CCGA[i]-4)==25):
				freqCCGA[25]+=1
			if((CCGA[i+j] - CCGA[i]-4)==26):
				freqCCGA[26]+=1
			if((CCGA[i+j] - CCGA[i]-4)==27):
				freqCCGA[27]+=1
			if((CCGA[i+j] - CCGA[i]-4)==28):
				freqCCGA[28]+=1
			if((CCGA[i+j] - CCGA[i]-4)==29):
				freqCCGA[29]+=1
			if((CCGA[i+j] - CCGA[i]-4)==30):
				freqCCGA[30]+=1

	for i in range (len(CCGAC)-1):
		for j in range(1-8):
			if(i+j>=len(ACGT)): break
			if((CCGAC[i+j] - CCGAC[i]-4)>30): break
			if((CCGAC[i+j] - CCGAC[i]-4)==0):
				freqCCGAC[0]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==1):
				freqCCGAC[1]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==2):
				freqCCGAC[2]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==3):
				freqCCGAC[3]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==4):
				freqCCGAC[4]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==5):
				freqCCGAC[5]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==6):
				freqCCGAC[6]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==7):
				freqCCGAC[7]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==8):
				freqCCGAC[8]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==9):
				freqCCGAC[9]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==10):
				freqCCGAC[10]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==11):
				freqCCGAC[11]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==12):
				freqCCGAC[12]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==13):
				freqCCGAC[13]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==14):
				freqCCGAC[14]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==15):
				freqCCGAC[15]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==16):
				freqCCGAC[16]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==17):
				freqCCGAC[17]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==18):
				freqCCGAC[18]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==19):
				freqCCGAC[19]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==20):
				freqCCGAC[20]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==21):
				freqCCGAC[21]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==22):
				freqCCGAC[22]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==23):
				freqCCGAC[23]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==24):
				freqCCGAC[24]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==25):
				freqCCGAC[25]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==26):
				freqCCGAC[26]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==27):
				freqCCGAC[27]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==28):
				freqCCGAC[28]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==29):
				freqCCGAC[29]+=1
			if((CCGAC[i+j] - CCGAC[i]-4)==30):
				freqCCGAC[30]+=1
"""
print "No of line traversed"
print noOfLines
print " "
print "Print freq of ACGT"
print freqACGT
print " "
print "Print freq of CCGA"		
print freqCCGA
print " "
print "Print freq of CCGAC"		
print freqCCGAC
print "*********************"															
