my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_dna[0:63]
intron = my_dna[63:90]
exon2 = my_dna[90:]
print(exon1 + intron.lower() + exon2)
