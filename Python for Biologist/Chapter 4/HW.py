# Processing DNA in file
data = open("exercises/input.txt")
trimmed = open("trimmed.txt", "w")

for dna in data:
    trim = dna[14:]
    trimmed.write(trim)
    print("Length of the processed sequence " + str(len(trim)))

trimmed.close()

# Multiple exons from genomic DNA
dna = open("exercises/genomic_dna.txt").read()
exon = open("exercises/exons.txt")
coding = ""

for line in exon:
    pos = line.split(',')    
    start = int(pos[0])
    stop = int(pos[1])
    exons = dna[start:stop]
    coding = coding + exons

print("Coding sequence is: " + coding)
out = open("coding.txt" , "w")
out.write(coding)
out.close()