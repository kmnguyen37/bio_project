import sys

#usage = sys.argv[0] + ": genome.fasta features.gff"

#if len(sys.argv) < 3:
 #   print(usage)
  #  sys.exit("\nThis script requires both a FASTA file and a GFF file\n")

#genome = sys.argv[1]
#gff    = sys.argv[2]

#data1 = open(genome, 'r')
#data2 = open(gff, 'r')

# Read FASTA file
data1 = open('watermelon.fsa', 'r')

# Variable that will hold the genome sequence
gen = ''

# Initialize a line counter
line_num = 0

# Read in the genome file
for line in data1:
    line = line.rstrip('\n')

    if line_num > 0:
        gen = gen + line

    # increment line_number
    line_num += 1

# Close the genome file
data1.close()

# Read GFF file
data2 = open('watermelon.gff', 'r')

# Variables for all the feature types 
CDS     = ''
tRNA    = ''
rRNA    = ''
IN      = ''
MF      = ''
RR      = ''

# read in the GFF file
for line in data2:

    # remove newline's - could also use strip
    line = line.rstrip('\n')

    types = line.split('; type ')
    other_type = types[len(types)-1]
    # print(other_type)
    
    cols = line.split('\t')
    type  = cols[2]
    start = int(cols[3])
    end   = int(cols[4])
    
    # print(type, "\t", start, "\t", end)

    # extract this feature from the genome
    fragment = gen[start-1:end]

    if type == 'CDS':
        CDS += fragment

    if type == 'intron':
        IN += fragment

    if type == 'misc_feature':
        MF += fragment

    if type == 'repeat_region':
        RR += fragment

    if type == 'rRNA':
        rRNA += fragment

    if type == 'tRNA':
        tRNA += fragment

# Length of feature types and genome sequence
gen1 = len(gen)
exon = len(CDS)
intron = len(IN)
misc = len(MF)
repeat = len(RR)
trna = len(tRNA)
rrna = len(rRNA)

# GC Content
GC_CDS = round((CDS.count('G') + CDS.count('C'))/exon*100, 2)
GC_RR  = round((RR.count('G') + RR.count('C'))/repeat*100, 2)
GC_MF  = round((MF.count('G') + MF.count('C'))/misc*100, 2)
GC_IN  = round((IN.count('G') + IN.count('C'))/intron*100, 2)
GC_tRNA  = round((tRNA.count('G') + tRNA.count('C'))/trna*100, 2)
GC_rRNA  = round((rRNA.count('G') + rRNA.count('C'))/rrna*100, 2)


# Percent of the genome covered by featured type
exon1 = round(exon/gen1*100, 2)
intron1 = round(intron/gen1*100, 2)
misc1 = round(misc/gen1*100, 2)
repeat1 = round(repeat/gen1*100, 2)
tr = round(trna/gen1*100, 2)
rr = round(rrna/gen1*100, 2)

# Print the output
print('CDS\t', exon, str(exon1) + '%', str(GC_CDS))
print('Intron\t', intron, str(intron1) + '%', str(GC_IN))
print('Misc Features\t', misc, str(misc1) + '%', str(GC_MF))
print('Repeat Region\t', repeat, str(repeat1) + '%', str(GC_RR))
print('tRNA\t', trna, str(tr) + '%', str(GC_tRNA))
print('rRNA\t', rrna, str(rr) + '%', str(GC_rRNA))

# Print A, T, G, C percent
print('CDS\t', str(round(CDS.count('A')/exon*100, 2)), 'A')
print('CDS\t', str(round(CDS.count('T')/exon*100, 2)), 'T')
print('CDS\t', str(round(CDS.count('G')/exon*100, 2)), 'G')
print('CDS\t', str(round(CDS.count('C')/exon*100, 2)), 'C')

print('Intron\t', str(round(IN.count('A')/intron*100, 2)), 'A')
print('Intron\t', str(round(IN.count('T')/intron*100, 2)), 'T')
print('Intron\t', str(round(IN.count('G')/intron*100, 2)), 'G')
print('Intron\t', str(round(IN.count('C')/intron*100, 2)), 'C')

print('MF\t', str(round(MF.count('A')/misc*100, 2)), 'A')
print('MF\t', str(round(MF.count('T')/misc*100, 2)), 'T')
print('MF\t', str(round(MF.count('G')/misc*100, 2)), 'G')
print('MF\t', str(round(MF.count('C')/misc*100, 2)), 'C')

print('RR\t', str(round(RR.count('A')/repeat*100, 2)), 'A')
print('RR\t', str(round(RR.count('T')/repeat*100, 2)), 'T')
print('RR\t', str(round(RR.count('G')/repeat*100, 2)), 'G')
print('RR\t', str(round(RR.count('C')/repeat*100, 2)), 'C')

print('rRNA\t', str(round(rRNA.count('A')/rrna*100, 2)), 'A')
print('rRNA\t', str(round(rRNA.count('T')/rrna*100, 2)), 'T')
print('rRNA\t', str(round(rRNA.count('G')/rrna*100, 2)), 'G')
print('rRNA\t', str(round(rRNA.count('C')/rrna*100, 2)), 'C')

print('tRNA\t', str(round(tRNA.count('A')/trna*100, 2)), 'A')
print('tRNA\t', str(round(tRNA.count('T')/trna*100, 2)), 'T')
print('tRNA\t', str(round(tRNA.count('G')/trna*100, 2)), 'G')
print('tRNA\t', str(round(tRNA.count('C')/trna*100, 2)), 'C')

# close the GFF file
data2.close()