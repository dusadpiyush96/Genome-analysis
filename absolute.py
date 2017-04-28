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

for line in l:
	noOfLines+=1
	line.upper
	ACGT=[]
	
	for n in xrange (len(line)-4):
		if (line[n:n+4]=="ACGT" ):
			ACGT.append(n)
			
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
	
	print "No of line traversed"
	print noOfLines
	print "Length of line"
	print len(line)
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
