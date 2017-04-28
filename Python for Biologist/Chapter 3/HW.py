# Spliting genomic DNA
dna = open("exercises/genomic_dna.txt")
mydna = dna.read()

exon1 = mydna[0:63]
exon2 = mydna[90:]
intron = mydna[63:90]

coding = open("exercises/coding_dna.txt", "w")
noncoding = open ("exercises/non_coding.txt", "w")

coding.write(exon1 + exon2)
noncoding.write(intron)

# Writing FASTA file
header1 = "ABC123"
header2 = "DEF456"
header3 = "HIJ789"

seq1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq2 = "actgatcgacgatcgatcgatcacgact"
seq3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

output = open("seq.fasta", "w")

output.write('>' + header1 + '\n' + seq1 + '\n')
output.write('>' + header2 + '\n' + seq2.upper() + '\n')
output.write('>' + header3 + '\n' + seq3.replace('-', '') + '\n')

# Writing multiple FASTA file
out1 = open("seq1.fasta", "w")
out1.write('>' + header1 + '\n' + seq1 + '\n')

out2 = open("seq2.fasta", "w")
out2.write('>' + header2 + '\n' + seq2.upper() + '\n')

out3 = open("seq3.fasta", "w")
out3.write('>' + header3 + '\n' + seq3.replace('-', '') + '\n')
