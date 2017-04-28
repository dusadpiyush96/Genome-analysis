l=open("WheatWholeGenomeLength.txt","r")
dna = l.readline()
noOfLines=0

loc0 = 0
loc1 = 0
loc2 = 0
loc3 = 0
loc4 = 0
loc5 = 0
loc6 = 0
loc7 = 0
loc8 = 0
loc9 = 0
loc10 = 0
loc11 = 0
loc12 = 0
loc13 = 0
loc14 = 0
loc15 = 0
loc16 = 0
loc17 = 0
loc18 = 0
loc19 = 0
loc20 = 0
loc21 = 0
loc22 = 0
loc23 = 0
loc24 = 0
loc25 = 0
loc26 = 0
loc27 = 0
loc28 = 0
loc29 = 0
loc30 = 0
	
locCCGAC0 = 0
locCCGAC1 = 0
locCCGAC2 = 0
locCCGAC3 = 0
locCCGAC4 = 0
locCCGAC5 = 0
locCCGAC6 = 0
locCCGAC7 = 0
locCCGAC8 = 0
locCCGAC9 = 0
locCCGAC10 = 0
locCCGAC11 = 0
locCCGAC12 = 0
locCCGAC13 = 0
locCCGAC14 = 0
locCCGAC15 = 0
locCCGAC16 = 0
locCCGAC17 = 0
locCCGAC18 = 0
locCCGAC19 = 0
locCCGAC20 = 0
locCCGAC21 = 0
locCCGAC22 = 0
locCCGAC23 = 0
locCCGAC24 = 0
locCCGAC25 = 0
locCCGAC26 = 0
locCCGAC27 = 0
locCCGAC28 = 0
locCCGAC29 = 0
locCCGAC30 = 0

locCCGA0 = 0
locCCGA1 = 0
locCCGA2 = 0
locCCGA3 = 0
locCCGA4 = 0
locCCGA5 = 0
locCCGA6 = 0
locCCGA7 = 0
locCCGA8 = 0
locCCGA9 = 0
locCCGA10 = 0
locCCGA11 = 0
locCCGA12 = 0
locCCGA13 = 0
locCCGA14 = 0
locCCGA15 = 0
locCCGA16 = 0
locCCGA17 = 0
locCCGA18 = 0
locCCGA19 = 0
locCCGA20 = 0
locCCGA21 = 0
locCCGA22 = 0
locCCGA23 = 0
locCCGA24 = 0
locCCGA25 = 0
locCCGA26 = 0
locCCGA27 = 0
locCCGA28 = 0
locCCGA29 = 0
locCCGA30 = 0
lengthsOfLines=[]

for line in l:
	noOfLines+=1
	#print line
	line.upper
	ACGT=[]
	CCGAC=[]
	CCGA=[]

	for n in xrange (len(line)-4):
		if (line[n:n+4]=="ACGT" ):
			ACGT.append(n)
			#noOfRepeats+=1

		if (line[n:n+4]=="CCGA" ):
		
			CCGA.append(n)
			#noOfRepeats+=1

		if (line[n:n+5]=="CCGAC" ):
		
			CCGAC.append(n)
			#noOfRepeats+=1
	




	for i in range (len(ACGT)-1):
		if((ACGT[i+1] - ACGT[i]-4)==0):
			loc0+=1
		if((ACGT[i+1] - ACGT[i]-4)==1):
			loc1+=1
		if((ACGT[i+1] - ACGT[i]-4)==2):
			loc2+=1
		if((ACGT[i+1] - ACGT[i]-4)==3):
			loc3+=1
		if((ACGT[i+1] - ACGT[i]-4)==4):
			loc4+=1
		if((ACGT[i+1] - ACGT[i]-4)==5):
			loc5+=1
		if((ACGT[i+1] - ACGT[i]-4)==6):
			loc6+=1
		if((ACGT[i+1] - ACGT[i]-4)==7):
			loc7+=1
		if((ACGT[i+1] - ACGT[i]-4)==8):
			loc8+=1
		if((ACGT[i+1] - ACGT[i]-4)==9):
			loc9+=1
		if((ACGT[i+1] - ACGT[i]-4)==10):
			loc10+=1
		if((ACGT[i+1] - ACGT[i]-4)==11):
			loc11+=1
		if((ACGT[i+1] - ACGT[i]-4)==12):
			loc12+=1
		if((ACGT[i+1] - ACGT[i]-4)==13):
			loc13+=1
		if((ACGT[i+1] - ACGT[i]-4)==14):
			loc14+=1
		if((ACGT[i+1] - ACGT[i]-4)==15):
			loc15+=1
		if((ACGT[i+1] - ACGT[i]-4)==16):
			loc16+=1
		if((ACGT[i+1] - ACGT[i]-4)==17):
			loc17+=1
		if((ACGT[i+1] - ACGT[i]-4)==18):
			loc18+=1
		if((ACGT[i+1] - ACGT[i]-4)==19):
			loc19+=1
		if((ACGT[i+1] - ACGT[i]-4)==20):
			loc20+=1
		if((ACGT[i+1] - ACGT[i]-4)==21):
			loc21+=1
		if((ACGT[i+1] - ACGT[i]-4)==22):
			loc22+=1
		if((ACGT[i+1] - ACGT[i]-4)==23):
			loc23+=1
		if((ACGT[i+1] - ACGT[i]-4)==24):
			loc24+=1
		if((ACGT[i+1] - ACGT[i]-4)==25):
			loc25+=1
		if((ACGT[i+1] - ACGT[i]-4)==26):
			loc26+=1
		if((ACGT[i+1] - ACGT[i]-4)==27):
			loc27+=1
		if((ACGT[i+1] - ACGT[i]-4)==28):
			loc28+=1
		if((ACGT[i+1] - ACGT[i]-4)==29):
			loc29+=1
		if((ACGT[i+1] - ACGT[i]-4)==30):
			loc30+=1
			
	for i in range (len(CCGA)-1):
		if((CCGA[i+1] - CCGA[i]-4)==0):
			locCCGA0+=1
		if((CCGA[i+1] - CCGA[i]-4)==1):
			locCCGA1+=1
		if((CCGA[i+1] - CCGA[i]-4)==2):
			locCCGA2+=1
		if((CCGA[i+1] - CCGA[i]-4)==3):
			locCCGA3+=1
		if((CCGA[i+1] - CCGA[i]-4)==4):
			locCCGA4+=1
		if((CCGA[i+1] - CCGA[i]-4)==5):
			locCCGA5+=1
		if((CCGA[i+1] - CCGA[i]-4)==6):
			locCCGA6+=1
		if((CCGA[i+1] - CCGA[i]-4)==7):
			locCCGA7+=1
		if((CCGA[i+1] - CCGA[i]-4)==8):
			locCCGA8+=1
		if((CCGA[i+1] - CCGA[i]-4)==9):
			locCCGA9+=1
		if((CCGA[i+1] - CCGA[i]-4)==10):
			locCCGA10+=1
		if((CCGA[i+1] - CCGA[i]-4)==11):
			locCCGA11+=1
		if((CCGA[i+1] - CCGA[i]-4)==12):
			locCCGA12+=1
		if((CCGA[i+1] - CCGA[i]-4)==13):
			locCCGA13+=1
		if((CCGA[i+1] - CCGA[i]-4)==14):
			locCCGA14+=1
		if((CCGA[i+1] - CCGA[i]-4)==15):
			locCCGA15+=1
		if((CCGA[i+1] - CCGA[i]-4)==16):
			locCCGA16+=1
		if((CCGA[i+1] - CCGA[i]-4)==17):
			locCCGA17+=1
		if((CCGA[i+1] - CCGA[i]-4)==18):
			locCCGA18+=1
		if((CCGA[i+1] - CCGA[i]-4)==19):
			locCCGA19+=1
		if((CCGA[i+1] - CCGA[i]-4)==20):
			locCCGA20+=1
		if((CCGA[i+1] - CCGA[i]-4)==21):
			locCCGA21+=1
		if((CCGA[i+1] - CCGA[i]-4)==22):
			locCCGA22+=1
		if((CCGA[i+1] - CCGA[i]-4)==23):
			locCCGA23+=1
		if((CCGA[i+1] - CCGA[i]-4)==24):
			locCCGA24+=1
		if((CCGA[i+1] - CCGA[i]-4)==25):
			locCCGA25+=1
		if((CCGA[i+1] - CCGA[i]-4)==26):
			locCCGA26+=1
		if((CCGA[i+1] - CCGA[i]-4)==27):
			locCCGA27+=1
		if((CCGA[i+1] - CCGA[i]-4)==28):
			locCCGA28+=1
		if((CCGA[i+1] - CCGA[i]-4)==29):
			locCCGA29+=1
		if((CCGA[i+1] - CCGA[i]-4)==30):
			locCCGA30+=1

	for i in range (len(CCGAC)-1):
		if((CCGAC[i+1] - CCGAC[i]-5)==0):
			locCCGAC0+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==1):
			locCCGAC1+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==2):
			locCCGAC2+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==3):
			locCCGAC3+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==4):
			locCCGAC4+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==5):
			locCCGAC5+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==6):
			locCCGAC6+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==7):
			locCCGAC7+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==8):
			locCCGAC8+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==9):
			locCCGAC9+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==10):
			locCCGAC10+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==11):
			locCCGAC11+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==12):
			locCCGAC12+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==13):
			locCCGAC13+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==14):
			locCCGAC14+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==15):
			locCCGAC15+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==16):
			locCCGAC16+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==17):
			locCCGAC17+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==18):
			locCCGAC18+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==19):
			locCCGAC19+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==20):
			locCCGAC20+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==21):
			locCCGAC21+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==22):
			locCCGAC22+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==23):
			locCCGAC23+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==24):
			locCCGAC24+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==25):
			locCCGAC25+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==26):
			locCCGAC26+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==27):
			locCCGAC27+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==28):
			locCCGAC28+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==29):
			locCCGAC29+=1
		if((CCGAC[i+1] - CCGAC[i]-5)==30):
			locCCGAC30+=1	

	print "No of line traversed"
	print noOfLines
	print "Length of line"
	print len(line)
	lengthsOfLines.append(len(line))
	print " "
	print "Print freq of ACGT"		
	print loc0
	print loc1
	print loc2
	print loc3
	print loc4
	print "fifth posn"
	print loc5
	print loc6
	print loc7
	print loc8
	print loc9
	print loc10
	print loc11
	print loc12
	print loc13
	print loc14
	print loc15
	print loc16
	print loc17
	print loc18
	print loc19
	print loc20
	print loc21
	print loc22
	print loc23
	print loc24
	print loc25
	print loc26
	print loc27
	print loc28
	print loc29
	print loc30	
	print "Print freq of CCGA"		
	print locCCGA0
	print locCCGA1
	print locCCGA2
	print locCCGA3
	print locCCGA4
	print locCCGA5
	print locCCGA6
	print locCCGA7
	print locCCGA8
	print locCCGA9
	print locCCGA10
	print locCCGA11
	print locCCGA12
	print locCCGA13
	print locCCGA14
	print locCCGA15
	print locCCGA16
	print locCCGA17
	print locCCGA18
	print locCCGA19
	print locCCGA20
	print locCCGA21
	print locCCGA22
	print locCCGA23
	print locCCGA24
	print locCCGA25
	print locCCGA26
	print locCCGA27
	print locCCGA28
	print locCCGA29
	print locCCGA30	
	print "Print freq of CCGAC"		
	print locCCGAC0
	print locCCGAC1
	print locCCGAC2
	print locCCGAC3
	print locCCGAC4
	print locCCGAC5
	print locCCGAC6
	print locCCGAC7
	print locCCGAC8
	print locCCGAC9
	print locCCGAC10
	print locCCGAC11
	print locCCGAC12
	print locCCGAC13
	print locCCGAC14
	print locCCGAC15
	print locCCGAC16
	print locCCGAC17
	print locCCGAC18
	print locCCGAC19
	print locCCGAC20
	print locCCGAC21
	print locCCGAC22
	print locCCGAC23
	print locCCGAC24
	print locCCGAC25
	print locCCGAC26
	print locCCGAC27
	print locCCGAC28
	print locCCGAC29
	print locCCGAC30	
	print "*********************"														

print "Number of lines"
dna=dna.upper()
#print dna.count("CCGA")
print noOfLines

noOfAat=[]    #this is the count of A at posn 1 for all the spacer length
noOfCat=[]
noOfGat=[]
noOfTat=[]
"""for i in range(30):
       noOfTat.append(0)
       noOfAat.append(0)
       noOfGat.append(0)
       noOfCat.append(0)
noOfRepeats=0
print len(dna)
for n in xrange (len(dna)-4):
	if (dna[n:n+4]=="ACGT" ):
		
		ACGT.append(n)
		noOfRepeats+=1
print noOfRepeats
print noOfLines"""
"""for n in range (len(ACGT)-1):
	if((ACGT[n+1]-ACGT[n]-4)==0 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[0]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==1 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[1]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==2 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[2]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==3 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[3]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==4 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[4]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==5 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[5]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==6 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[6]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==7 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[7]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==8 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[8]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==9 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[9]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==10 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[10]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==11 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[11]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==12 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[12]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==13 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[13]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==14 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[14]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==15 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[15]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==16 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[16]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==17 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[17]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==18 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[18]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==19 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[19]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==20 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[20]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==21 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[21]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==22 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[22]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==23 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[23]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==24 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[24]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==25 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[25]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==26 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[26]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==27 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[27]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==28 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[28]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==29 and (dna[(ACGT[n])+4]=='T')):
		noOfTat[29]+=1;




	
	if((ACGT[n+1]-ACGT[n]-4)==0 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[0]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==1 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[1]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==2 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[2]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==3 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[3]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==4 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[4]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==5 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[5]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==6 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[6]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==7 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[7]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==8 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[8]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==9 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[9]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==10 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[10]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==11 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[11]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==12 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[12]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==13 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[13]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==14 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[14]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==15 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[15]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==16 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[16]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==17 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[17]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==18 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[18]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==19 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[19]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==20 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[20]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==21 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[21]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==22 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[22]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==23 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[23]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==24 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[24]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==25 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[25]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==26 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[26]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==27 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[27]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==28 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[28]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==29 and (dna[(ACGT[n])+4]=='G')):
		noOfGat[29]+=1;	
	

















	if((ACGT[n+1]-ACGT[n]-4)==0 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[0]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==1 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[1]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==2 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[2]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==3 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[3]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==4 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[4]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==5 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[5]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==6 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[6]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==7 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[7]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==8 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[8]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==9 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[9]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==10 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[10]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==11 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[11]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==12 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[12]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==13 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[13]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==14 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[14]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==15 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[15]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==16 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[16]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==17 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[17]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==18 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[18]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==19 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[19]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==20 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[20]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==21 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[21]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==22 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[22]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==23 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[23]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==24 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[24]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==25 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[25]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==26 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[26]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==27 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[27]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==28 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[28]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==29 and (dna[(ACGT[n])+4]=='A')):
		noOfAat[29]+=1;




	if((ACGT[n+1]-ACGT[n]-4)==0 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[0]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==1 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[1]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==2 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[2]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==3 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[3]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==4 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[4]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==5 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[5]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==6 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[6]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==7 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[7]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==8 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[8]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==9 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[9]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==10 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[10]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==11 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[11]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==12 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[12]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==13 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[13]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==14 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[14]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==15 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[15]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==16 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[16]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==17 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[17]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==18 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[18]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==19 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[19]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==20 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[20]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==21 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[21]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==22 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[22]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==23 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[23]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==24 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[24]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==25 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[25]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==26 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[26]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==27 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[27]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==28 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[28]+=1;
	if((ACGT[n+1]-ACGT[n]-4)==29 and (dna[(ACGT[n])+4]=='C')):
		noOfCat[29]+=1;

#print noOfCat[7]
print noOfAat
print noOfCat
print noOfTat
print noOfGat"""
"""for i in range (len(ACGT)-1):
	if((ACGT[i+1] - ACGT[i]-4)==0):
		loc0+=1
	if((ACGT[i+1] - ACGT[i]-4)==1):
		loc1+=1
	if((ACGT[i+1] - ACGT[i]-4)==2):
		loc2+=1
	if((ACGT[i+1] - ACGT[i]-4)==3):
		loc3+=1

	if((ACGT[i+1] - ACGT[i]-4)==4):
		loc4+=1
	if((ACGT[i+1] - ACGT[i]-4)==5):
		loc5+=1
	if((ACGT[i+1] - ACGT[i]-4)==6):
		loc6+=1
	if((ACGT[i+1] - ACGT[i]-4)==7):
		loc7+=1
	if((ACGT[i+1] - ACGT[i]-4)==8):
		loc8+=1
	if((ACGT[i+1] - ACGT[i]-4)==9):
		loc9+=1
	if((ACGT[i+1] - ACGT[i]-4)==10):
		loc10+=1
	if((ACGT[i+1] - ACGT[i]-4)==11):
		loc11+=1
	if((ACGT[i+1] - ACGT[i]-4)==12):
		loc12+=1
	if((ACGT[i+1] - ACGT[i]-4)==13):
		loc13+=1
	if((ACGT[i+1] - ACGT[i]-4)==14):
		loc14+=1
	if((ACGT[i+1] - ACGT[i]-4)==15):
		loc15+=1
	if((ACGT[i+1] - ACGT[i]-4)==16):
		loc16+=1
	if((ACGT[i+1] - ACGT[i]-4)==17):
		loc17+=1
	if((ACGT[i+1] - ACGT[i]-4)==18):
		loc18+=1
	if((ACGT[i+1] - ACGT[i]-4)==19):
		loc19+=1
	if((ACGT[i+1] - ACGT[i]-4)==20):
		loc20+=1
	if((ACGT[i+1] - ACGT[i]-4)==21):
		loc21+=1
	if((ACGT[i+1] - ACGT[i]-4)==22):
		loc22+=1
	if((ACGT[i+1] - ACGT[i]-4)==23):
		loc23+=1
	if((ACGT[i+1] - ACGT[i]-4)==24):
		loc24+=1
	if((ACGT[i+1] - ACGT[i]-4)==25):
		loc25+=1
	if((ACGT[i+1] - ACGT[i]-4)==26):
		loc26+=1
	if((ACGT[i+1] - ACGT[i]-4)==27):
		loc27+=1
	if((ACGT[i+1] - ACGT[i]-4)==28):
		loc28+=1
	if((ACGT[i+1] - ACGT[i]-4)==29):
		loc29+=1
	if((ACGT[i+1] - ACGT[i]-4)==30):
		loc30+=1
#print loc5																
print loc0
print loc1
print loc2
print loc3
print loc4
print loc5
print loc6
print loc7
print loc8
print loc9
print loc10
print loc11
print loc12
print loc13
print loc14
print loc15
print loc16
print loc17
print loc18
print loc19
print loc20
print loc21
print loc22
print loc23
print loc24
print loc25
print loc26
print loc27
print loc28
print loc29
print loc30

#print noOfRepeats"""

