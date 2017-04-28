l=open("WheatWholeGenomeLength.txt","r")
dna = l.read()
dna=dna.upper()
#print dna.count("CCGA")
piyush=[]
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
noOfAat=[]    #this is the count of A at posn 1 for all the spacer length
noOfCat=[]
noOfGat=[]
noOfTat=[]
for i in range(30):
       noOfTat.append(0)
       noOfAat.append(0)
       noOfGat.append(0)
       noOfCat.append(0)
noOfRepeats=0
print len(dna)
for n in xrange (len(dna)-4):
	if (dna[n:n+4]=="ACGT" ):
		
		piyush.append(n)
		noOfRepeats+=1
print noOfRepeats
"""for n in range (len(piyush)-1):
	if((piyush[n+1]-piyush[n]-4)==0 and (dna[(piyush[n])+4]=='T')):
		noOfTat[0]+=1;
	if((piyush[n+1]-piyush[n]-4)==1 and (dna[(piyush[n])+4]=='T')):
		noOfTat[1]+=1;
	if((piyush[n+1]-piyush[n]-4)==2 and (dna[(piyush[n])+4]=='T')):
		noOfTat[2]+=1;
	if((piyush[n+1]-piyush[n]-4)==3 and (dna[(piyush[n])+4]=='T')):
		noOfTat[3]+=1;
	if((piyush[n+1]-piyush[n]-4)==4 and (dna[(piyush[n])+4]=='T')):
		noOfTat[4]+=1;
	if((piyush[n+1]-piyush[n]-4)==5 and (dna[(piyush[n])+4]=='T')):
		noOfTat[5]+=1;
	if((piyush[n+1]-piyush[n]-4)==6 and (dna[(piyush[n])+4]=='T')):
		noOfTat[6]+=1;
	if((piyush[n+1]-piyush[n]-4)==7 and (dna[(piyush[n])+4]=='T')):
		noOfTat[7]+=1;
	if((piyush[n+1]-piyush[n]-4)==8 and (dna[(piyush[n])+4]=='T')):
		noOfTat[8]+=1;
	if((piyush[n+1]-piyush[n]-4)==9 and (dna[(piyush[n])+4]=='T')):
		noOfTat[9]+=1;
	if((piyush[n+1]-piyush[n]-4)==10 and (dna[(piyush[n])+4]=='T')):
		noOfTat[10]+=1;
	if((piyush[n+1]-piyush[n]-4)==11 and (dna[(piyush[n])+4]=='T')):
		noOfTat[11]+=1;
	if((piyush[n+1]-piyush[n]-4)==12 and (dna[(piyush[n])+4]=='T')):
		noOfTat[12]+=1;
	if((piyush[n+1]-piyush[n]-4)==13 and (dna[(piyush[n])+4]=='T')):
		noOfTat[13]+=1;
	if((piyush[n+1]-piyush[n]-4)==14 and (dna[(piyush[n])+4]=='T')):
		noOfTat[14]+=1;
	if((piyush[n+1]-piyush[n]-4)==15 and (dna[(piyush[n])+4]=='T')):
		noOfTat[15]+=1;
	if((piyush[n+1]-piyush[n]-4)==16 and (dna[(piyush[n])+4]=='T')):
		noOfTat[16]+=1;
	if((piyush[n+1]-piyush[n]-4)==17 and (dna[(piyush[n])+4]=='T')):
		noOfTat[17]+=1;
	if((piyush[n+1]-piyush[n]-4)==18 and (dna[(piyush[n])+4]=='T')):
		noOfTat[18]+=1;
	if((piyush[n+1]-piyush[n]-4)==19 and (dna[(piyush[n])+4]=='T')):
		noOfTat[19]+=1;
	if((piyush[n+1]-piyush[n]-4)==20 and (dna[(piyush[n])+4]=='T')):
		noOfTat[20]+=1;
	if((piyush[n+1]-piyush[n]-4)==21 and (dna[(piyush[n])+4]=='T')):
		noOfTat[21]+=1;
	if((piyush[n+1]-piyush[n]-4)==22 and (dna[(piyush[n])+4]=='T')):
		noOfTat[22]+=1;
	if((piyush[n+1]-piyush[n]-4)==23 and (dna[(piyush[n])+4]=='T')):
		noOfTat[23]+=1;
	if((piyush[n+1]-piyush[n]-4)==24 and (dna[(piyush[n])+4]=='T')):
		noOfTat[24]+=1;
	if((piyush[n+1]-piyush[n]-4)==25 and (dna[(piyush[n])+4]=='T')):
		noOfTat[25]+=1;
	if((piyush[n+1]-piyush[n]-4)==26 and (dna[(piyush[n])+4]=='T')):
		noOfTat[26]+=1;
	if((piyush[n+1]-piyush[n]-4)==27 and (dna[(piyush[n])+4]=='T')):
		noOfTat[27]+=1;
	if((piyush[n+1]-piyush[n]-4)==28 and (dna[(piyush[n])+4]=='T')):
		noOfTat[28]+=1;
	if((piyush[n+1]-piyush[n]-4)==29 and (dna[(piyush[n])+4]=='T')):
		noOfTat[29]+=1;




	
	if((piyush[n+1]-piyush[n]-4)==0 and (dna[(piyush[n])+4]=='G')):
		noOfGat[0]+=1;
	if((piyush[n+1]-piyush[n]-4)==1 and (dna[(piyush[n])+4]=='G')):
		noOfGat[1]+=1;
	if((piyush[n+1]-piyush[n]-4)==2 and (dna[(piyush[n])+4]=='G')):
		noOfGat[2]+=1;
	if((piyush[n+1]-piyush[n]-4)==3 and (dna[(piyush[n])+4]=='G')):
		noOfGat[3]+=1;
	if((piyush[n+1]-piyush[n]-4)==4 and (dna[(piyush[n])+4]=='G')):
		noOfGat[4]+=1;
	if((piyush[n+1]-piyush[n]-4)==5 and (dna[(piyush[n])+4]=='G')):
		noOfGat[5]+=1;
	if((piyush[n+1]-piyush[n]-4)==6 and (dna[(piyush[n])+4]=='G')):
		noOfGat[6]+=1;
	if((piyush[n+1]-piyush[n]-4)==7 and (dna[(piyush[n])+4]=='G')):
		noOfGat[7]+=1;
	if((piyush[n+1]-piyush[n]-4)==8 and (dna[(piyush[n])+4]=='G')):
		noOfGat[8]+=1;
	if((piyush[n+1]-piyush[n]-4)==9 and (dna[(piyush[n])+4]=='G')):
		noOfGat[9]+=1;
	if((piyush[n+1]-piyush[n]-4)==10 and (dna[(piyush[n])+4]=='G')):
		noOfGat[10]+=1;
	if((piyush[n+1]-piyush[n]-4)==11 and (dna[(piyush[n])+4]=='G')):
		noOfGat[11]+=1;
	if((piyush[n+1]-piyush[n]-4)==12 and (dna[(piyush[n])+4]=='G')):
		noOfGat[12]+=1;
	if((piyush[n+1]-piyush[n]-4)==13 and (dna[(piyush[n])+4]=='G')):
		noOfGat[13]+=1;
	if((piyush[n+1]-piyush[n]-4)==14 and (dna[(piyush[n])+4]=='G')):
		noOfGat[14]+=1;
	if((piyush[n+1]-piyush[n]-4)==15 and (dna[(piyush[n])+4]=='G')):
		noOfGat[15]+=1;
	if((piyush[n+1]-piyush[n]-4)==16 and (dna[(piyush[n])+4]=='G')):
		noOfGat[16]+=1;
	if((piyush[n+1]-piyush[n]-4)==17 and (dna[(piyush[n])+4]=='G')):
		noOfGat[17]+=1;
	if((piyush[n+1]-piyush[n]-4)==18 and (dna[(piyush[n])+4]=='G')):
		noOfGat[18]+=1;
	if((piyush[n+1]-piyush[n]-4)==19 and (dna[(piyush[n])+4]=='G')):
		noOfGat[19]+=1;
	if((piyush[n+1]-piyush[n]-4)==20 and (dna[(piyush[n])+4]=='G')):
		noOfGat[20]+=1;
	if((piyush[n+1]-piyush[n]-4)==21 and (dna[(piyush[n])+4]=='G')):
		noOfGat[21]+=1;
	if((piyush[n+1]-piyush[n]-4)==22 and (dna[(piyush[n])+4]=='G')):
		noOfGat[22]+=1;
	if((piyush[n+1]-piyush[n]-4)==23 and (dna[(piyush[n])+4]=='G')):
		noOfGat[23]+=1;
	if((piyush[n+1]-piyush[n]-4)==24 and (dna[(piyush[n])+4]=='G')):
		noOfGat[24]+=1;
	if((piyush[n+1]-piyush[n]-4)==25 and (dna[(piyush[n])+4]=='G')):
		noOfGat[25]+=1;
	if((piyush[n+1]-piyush[n]-4)==26 and (dna[(piyush[n])+4]=='G')):
		noOfGat[26]+=1;
	if((piyush[n+1]-piyush[n]-4)==27 and (dna[(piyush[n])+4]=='G')):
		noOfGat[27]+=1;
	if((piyush[n+1]-piyush[n]-4)==28 and (dna[(piyush[n])+4]=='G')):
		noOfGat[28]+=1;
	if((piyush[n+1]-piyush[n]-4)==29 and (dna[(piyush[n])+4]=='G')):
		noOfGat[29]+=1;	
	

















	if((piyush[n+1]-piyush[n]-4)==0 and (dna[(piyush[n])+4]=='A')):
		noOfAat[0]+=1;
	if((piyush[n+1]-piyush[n]-4)==1 and (dna[(piyush[n])+4]=='A')):
		noOfAat[1]+=1;
	if((piyush[n+1]-piyush[n]-4)==2 and (dna[(piyush[n])+4]=='A')):
		noOfAat[2]+=1;
	if((piyush[n+1]-piyush[n]-4)==3 and (dna[(piyush[n])+4]=='A')):
		noOfAat[3]+=1;
	if((piyush[n+1]-piyush[n]-4)==4 and (dna[(piyush[n])+4]=='A')):
		noOfAat[4]+=1;
	if((piyush[n+1]-piyush[n]-4)==5 and (dna[(piyush[n])+4]=='A')):
		noOfAat[5]+=1;
	if((piyush[n+1]-piyush[n]-4)==6 and (dna[(piyush[n])+4]=='A')):
		noOfAat[6]+=1;
	if((piyush[n+1]-piyush[n]-4)==7 and (dna[(piyush[n])+4]=='A')):
		noOfAat[7]+=1;
	if((piyush[n+1]-piyush[n]-4)==8 and (dna[(piyush[n])+4]=='A')):
		noOfAat[8]+=1;
	if((piyush[n+1]-piyush[n]-4)==9 and (dna[(piyush[n])+4]=='A')):
		noOfAat[9]+=1;
	if((piyush[n+1]-piyush[n]-4)==10 and (dna[(piyush[n])+4]=='A')):
		noOfAat[10]+=1;
	if((piyush[n+1]-piyush[n]-4)==11 and (dna[(piyush[n])+4]=='A')):
		noOfAat[11]+=1;
	if((piyush[n+1]-piyush[n]-4)==12 and (dna[(piyush[n])+4]=='A')):
		noOfAat[12]+=1;
	if((piyush[n+1]-piyush[n]-4)==13 and (dna[(piyush[n])+4]=='A')):
		noOfAat[13]+=1;
	if((piyush[n+1]-piyush[n]-4)==14 and (dna[(piyush[n])+4]=='A')):
		noOfAat[14]+=1;
	if((piyush[n+1]-piyush[n]-4)==15 and (dna[(piyush[n])+4]=='A')):
		noOfAat[15]+=1;
	if((piyush[n+1]-piyush[n]-4)==16 and (dna[(piyush[n])+4]=='A')):
		noOfAat[16]+=1;
	if((piyush[n+1]-piyush[n]-4)==17 and (dna[(piyush[n])+4]=='A')):
		noOfAat[17]+=1;
	if((piyush[n+1]-piyush[n]-4)==18 and (dna[(piyush[n])+4]=='A')):
		noOfAat[18]+=1;
	if((piyush[n+1]-piyush[n]-4)==19 and (dna[(piyush[n])+4]=='A')):
		noOfAat[19]+=1;
	if((piyush[n+1]-piyush[n]-4)==20 and (dna[(piyush[n])+4]=='A')):
		noOfAat[20]+=1;
	if((piyush[n+1]-piyush[n]-4)==21 and (dna[(piyush[n])+4]=='A')):
		noOfAat[21]+=1;
	if((piyush[n+1]-piyush[n]-4)==22 and (dna[(piyush[n])+4]=='A')):
		noOfAat[22]+=1;
	if((piyush[n+1]-piyush[n]-4)==23 and (dna[(piyush[n])+4]=='A')):
		noOfAat[23]+=1;
	if((piyush[n+1]-piyush[n]-4)==24 and (dna[(piyush[n])+4]=='A')):
		noOfAat[24]+=1;
	if((piyush[n+1]-piyush[n]-4)==25 and (dna[(piyush[n])+4]=='A')):
		noOfAat[25]+=1;
	if((piyush[n+1]-piyush[n]-4)==26 and (dna[(piyush[n])+4]=='A')):
		noOfAat[26]+=1;
	if((piyush[n+1]-piyush[n]-4)==27 and (dna[(piyush[n])+4]=='A')):
		noOfAat[27]+=1;
	if((piyush[n+1]-piyush[n]-4)==28 and (dna[(piyush[n])+4]=='A')):
		noOfAat[28]+=1;
	if((piyush[n+1]-piyush[n]-4)==29 and (dna[(piyush[n])+4]=='A')):
		noOfAat[29]+=1;




	if((piyush[n+1]-piyush[n]-4)==0 and (dna[(piyush[n])+4]=='C')):
		noOfCat[0]+=1;
	if((piyush[n+1]-piyush[n]-4)==1 and (dna[(piyush[n])+4]=='C')):
		noOfCat[1]+=1;
	if((piyush[n+1]-piyush[n]-4)==2 and (dna[(piyush[n])+4]=='C')):
		noOfCat[2]+=1;
	if((piyush[n+1]-piyush[n]-4)==3 and (dna[(piyush[n])+4]=='C')):
		noOfCat[3]+=1;
	if((piyush[n+1]-piyush[n]-4)==4 and (dna[(piyush[n])+4]=='C')):
		noOfCat[4]+=1;
	if((piyush[n+1]-piyush[n]-4)==5 and (dna[(piyush[n])+4]=='C')):
		noOfCat[5]+=1;
	if((piyush[n+1]-piyush[n]-4)==6 and (dna[(piyush[n])+4]=='C')):
		noOfCat[6]+=1;
	if((piyush[n+1]-piyush[n]-4)==7 and (dna[(piyush[n])+4]=='C')):
		noOfCat[7]+=1;
	if((piyush[n+1]-piyush[n]-4)==8 and (dna[(piyush[n])+4]=='C')):
		noOfCat[8]+=1;
	if((piyush[n+1]-piyush[n]-4)==9 and (dna[(piyush[n])+4]=='C')):
		noOfCat[9]+=1;
	if((piyush[n+1]-piyush[n]-4)==10 and (dna[(piyush[n])+4]=='C')):
		noOfCat[10]+=1;
	if((piyush[n+1]-piyush[n]-4)==11 and (dna[(piyush[n])+4]=='C')):
		noOfCat[11]+=1;
	if((piyush[n+1]-piyush[n]-4)==12 and (dna[(piyush[n])+4]=='C')):
		noOfCat[12]+=1;
	if((piyush[n+1]-piyush[n]-4)==13 and (dna[(piyush[n])+4]=='C')):
		noOfCat[13]+=1;
	if((piyush[n+1]-piyush[n]-4)==14 and (dna[(piyush[n])+4]=='C')):
		noOfCat[14]+=1;
	if((piyush[n+1]-piyush[n]-4)==15 and (dna[(piyush[n])+4]=='C')):
		noOfCat[15]+=1;
	if((piyush[n+1]-piyush[n]-4)==16 and (dna[(piyush[n])+4]=='C')):
		noOfCat[16]+=1;
	if((piyush[n+1]-piyush[n]-4)==17 and (dna[(piyush[n])+4]=='C')):
		noOfCat[17]+=1;
	if((piyush[n+1]-piyush[n]-4)==18 and (dna[(piyush[n])+4]=='C')):
		noOfCat[18]+=1;
	if((piyush[n+1]-piyush[n]-4)==19 and (dna[(piyush[n])+4]=='C')):
		noOfCat[19]+=1;
	if((piyush[n+1]-piyush[n]-4)==20 and (dna[(piyush[n])+4]=='C')):
		noOfCat[20]+=1;
	if((piyush[n+1]-piyush[n]-4)==21 and (dna[(piyush[n])+4]=='C')):
		noOfCat[21]+=1;
	if((piyush[n+1]-piyush[n]-4)==22 and (dna[(piyush[n])+4]=='C')):
		noOfCat[22]+=1;
	if((piyush[n+1]-piyush[n]-4)==23 and (dna[(piyush[n])+4]=='C')):
		noOfCat[23]+=1;
	if((piyush[n+1]-piyush[n]-4)==24 and (dna[(piyush[n])+4]=='C')):
		noOfCat[24]+=1;
	if((piyush[n+1]-piyush[n]-4)==25 and (dna[(piyush[n])+4]=='C')):
		noOfCat[25]+=1;
	if((piyush[n+1]-piyush[n]-4)==26 and (dna[(piyush[n])+4]=='C')):
		noOfCat[26]+=1;
	if((piyush[n+1]-piyush[n]-4)==27 and (dna[(piyush[n])+4]=='C')):
		noOfCat[27]+=1;
	if((piyush[n+1]-piyush[n]-4)==28 and (dna[(piyush[n])+4]=='C')):
		noOfCat[28]+=1;
	if((piyush[n+1]-piyush[n]-4)==29 and (dna[(piyush[n])+4]=='C')):
		noOfCat[29]+=1;

#print noOfCat[7]
print noOfAat
print noOfCat
print noOfTat
print noOfGat"""
for i in range (len(piyush)-1):
	if((piyush[i+1] - piyush[i]-4)==0):
		loc0+=1
	if((piyush[i+1] - piyush[i]-4)==1):
		loc1+=1
	if((piyush[i+1] - piyush[i]-4)==2):
		loc2+=1
	if((piyush[i+1] - piyush[i]-4)==3):
		loc3+=1

	if((piyush[i+1] - piyush[i]-4)==4):
		loc4+=1
	if((piyush[i+1] - piyush[i]-4)==5):
		loc5+=1
	if((piyush[i+1] - piyush[i]-4)==6):
		loc6+=1
	if((piyush[i+1] - piyush[i]-4)==7):
		loc7+=1
	if((piyush[i+1] - piyush[i]-4)==8):
		loc8+=1
	if((piyush[i+1] - piyush[i]-4)==9):
		loc9+=1
	if((piyush[i+1] - piyush[i]-4)==10):
		loc10+=1
	if((piyush[i+1] - piyush[i]-4)==11):
		loc11+=1
	if((piyush[i+1] - piyush[i]-4)==12):
		loc12+=1
	if((piyush[i+1] - piyush[i]-4)==13):
		loc13+=1
	if((piyush[i+1] - piyush[i]-4)==14):
		loc14+=1
	if((piyush[i+1] - piyush[i]-4)==15):
		loc15+=1
	if((piyush[i+1] - piyush[i]-4)==16):
		loc16+=1
	if((piyush[i+1] - piyush[i]-4)==17):
		loc17+=1
	if((piyush[i+1] - piyush[i]-4)==18):
		loc18+=1
	if((piyush[i+1] - piyush[i]-4)==19):
		loc19+=1
	if((piyush[i+1] - piyush[i]-4)==20):
		loc20+=1
	if((piyush[i+1] - piyush[i]-4)==21):
		loc21+=1
	if((piyush[i+1] - piyush[i]-4)==22):
		loc22+=1
	if((piyush[i+1] - piyush[i]-4)==23):
		loc23+=1
	if((piyush[i+1] - piyush[i]-4)==24):
		loc24+=1
	if((piyush[i+1] - piyush[i]-4)==25):
		loc25+=1
	if((piyush[i+1] - piyush[i]-4)==26):
		loc26+=1
	if((piyush[i+1] - piyush[i]-4)==27):
		loc27+=1
	if((piyush[i+1] - piyush[i]-4)==28):
		loc28+=1
	if((piyush[i+1] - piyush[i]-4)==29):
		loc29+=1
	if((piyush[i+1] - piyush[i]-4)==30):
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

#print noOfRepeats

