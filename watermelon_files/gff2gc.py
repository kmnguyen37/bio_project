# Load the system module
import sys

hi = 37

# Function to clean up DNA sequence
def clean_seq(input_seq):
    #global hi
    #print('Function-1:', hi)
    #hi += 1
    #print('Functino-2:', hi)
    clean = input_seq.upper()
    clean = clean.replace('N', '')
    return (clean) 

def nuc_seq(sequence, base, sig_digs=2):
    # Calulate the length of the sequnce
    length = len(sequence)
    # Count the number of this nucleotide
    count_of_base = sequence.count(base)
    #Frequency of base
    freq_of_base = round(count_of_base/length, 2)
    # Return the frequency and the length
    return(length, freq_of_base)

# Declare the file names
gff_file = 'watermelon.gff'
fsa_file = 'watermelon.fsa'

# Open the files for reading
gff_in = open(gff_file, 'r')
fsa_in = open(fsa_file, 'r')

# Declare variable that will hold the genome sequence
genome = ''

# Initialize a line counter
line_number = 0

# Read in the genome file
for line in fsa_in:
    # Remove newline's - could also use strip
    line = line.rstrip('\n')

    if line_number > 0:
        genome = genome + line

    # Increment line_number
    line_number += 1

# Close the genome file
fsa_in.close()

cds     = ''
trna    = ''
rrna    = ''
intron  = ''
misc    = ''
repeats = ''

# Read in the GFF file
for line in gff_in:

    # Remove newline's - could also use strip
    line = line.rstrip('\n')

    types = line.split('; type ')
    other_type = types[len(types)-1]
    # print(other_type)
    
    fields = line.split('\t')
    type  = fields[2]
    start = int(fields[3])
    end   = int(fields[4])
    
    # Extract this feature from the genome
    fragment = genome[start-1:end]
    
    fragment = clean_seq(fragment)
    
    list_of_features = ['CDS', 'intron', 'misc_features', 'repeat_regions', 'rRNA', 'tRNA']
    for feature_types in list_of_features:
        if type == feature_types:
            feature_types += fragment
        for nucleotide in ['A', 'T', 'C', 'G']:
            # Calcukate the nuclotide composition for each feature:
                (feature_length, feature_comp) = nuc_seq(type, nucleotide, sig_digs=2)
print(feature_types + '\t' + str(feature_length) + '\t' + str(feature_comp*100) + '%\t' + nucleotide)  

# Close the GFF file
gff_in.close()
