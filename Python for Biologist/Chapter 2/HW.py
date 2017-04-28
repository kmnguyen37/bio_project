mydna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

# Calculating AT content
length = len(mydna)
A_count = mydna.count('A')
T_count = mydna.count('T')
at_content = (A_count+T_count)/length

print("The length of this DNA is " + str(length))
print("The number of A is " + str(A_count))
print("The number of T is " + str(T_count))
print("The AT content in this DNA is " + str(at_content))

# Complementing DNA
At = mydna.replace('A', 't')
Ta = At.replace('T', 'a')
Gc = Ta.replace('G', 'c')
Cg = Gc.replace('C', 'g')
print(Cg.upper())

# Restriction fragment lengths
dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
frag1 = dna.find("GAATTC") + 1
frag2 = len(dna) - frag1
print("The length of fragment 1 is " + str(frag1))
print("The length of fragment 2 is " + str(frag2))

# Slicing out introns
dna1 = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = dna1[0:63]
exon2 = dna1[90:]
intron = dna1[63:90].lower()
coding = len(exon1 + exon2)
length = len(dna1)
cp = round(coding/length*100, 1)
print("The coding percent is " + str(cp))
print(exon1+intron+exon2)