# This script reads and parse collection data for a new ctenophore species

data = open("Marrus.txt")

# Create line counter
line_number = 0

# Create loops in file
for line in data:
    # Stripping the new line at the end of the line
    line = line.rstrip("\n")
    
    # Not reading the first line
    if line_number > 0:
        print(str(line_number) + ": " + line)
    
    line_number += 1