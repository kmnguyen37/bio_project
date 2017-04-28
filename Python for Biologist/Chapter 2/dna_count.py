# This script calculates the nucleotide compostition of DNA sequence

dna = "    ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT   "

# Replace the "space" by nothing
dna = dna.replace(' ','')

# Change to all uppercase letter
dna = dna.upper()

length = len(dna)
Ap = round(dna.count('A')/length*100, 2)
Tp = round(dna.count('T')/length*100, 2)
Gp = round(dna.count('G')/length*100, 2)
Cp = round(dna.count('C')/length*100, 2)

print("length: " + str(length))
print("A percent: " + str(Ap) +'%')
print("T percent: " + str(Tp) +'%')
print("G percent: " + str(Gp) +'%')
print("C percent: " + str(Cp) +'%')

print(Ap+Tp+Gp+Cp)

