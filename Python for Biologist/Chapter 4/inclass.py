# LISTING
number = [0, 1, 2, 3, 4, 5, 6,7]

# Grab and print the first 3 elements
print(number[0:3])

# Grab and print 3, 4, 5
print(number[3:6])

# Grab and print 5, 6, 7
print(number[5:])

# Grab and print the first 2 elements
print(number[0:2])

mydna = "ATGCCAGTttccggaaGTTCTAA" #23
exon1 = "ATGCCAGT" #8
intron = "ttccggaa" #7
exon2 = "GTTCTAA" #8

lens = len(mydna)
len1 = len(exon1)
len2 = len(exon2)
leni = len(intron)

# grab and print the first exon
print("The first exon is " + exon1)
print(mydna[:8])

# Grab and print the intron
print("The intron is " + intron)
print(mydna[9:16])

# Grab and print the second exon
print("The second exon is " + exon2)
print(mydna[16:])

# Grab and print the start codon
print(mydna[0:3])

# Grab and pront the stop codon
print(mydna[20:])

with open("bob.txt", 'r') as f:
    bob = f.read()

songs = []
for line in bob:
    line = line.strip('\n')
    