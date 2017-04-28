# Declaring file
fsa = 'watermelon.fsa'
gff = 'watermelon.gff'

# Open FSA and GFF file
data1 = open(fsa, 'r')
data2 = open(gff, 'r')

# Declaring a variable
gen = ''

# Initiate line number
line_number = 0

# Read in genome file
for line in data1:
    #remove newline
    line = line.rstrip('\n')
    
    if line_number > 0:
        gen = gen + line
        
    #increment line number
    line_number += 1
 

# Close fsa file
data1.close()

# read in the gff file
for line in data2:
    types = line.split(': types ')
    other_type = types[len(types)-1]
    
    col = line.split('\t')
    ft = col[2]
    start = int(col[3])
    end = int(col[4])
    
    # extract this features from the genome
    frag = gen[start-1:end]
    