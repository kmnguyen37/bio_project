# Function to clean up data sequence
def clean_seq(input_seq):
    clean = input_seq.upper()
    clean = clean.replace('N', '')
    return clean 