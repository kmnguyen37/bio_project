# Import module for regular expression
import re

# Searching for a pattern in a string
dna = "ATCGCGAATTCAC"
if re.search(r"GAATTC", dna):
    print("restriction site found!")
    
dna = "ATCGCGAATTCAC"
if re.search(r"GG(A|T)CC", dna):
    print("restriction site found!")
    
# Character group
dna = "ATCGCGAATTCAC"
if re.search(r"GC[ATGC]GC", dna):
    print("restriction site found!")

# Extracting part of the string that matched
dna = "ATGACGTACGTACGACTG"
## store the match object in the variable m
m = re.search(r"GA[ATGC]{3}AC", dna)
print(m.group())

dna = "ATGACGTACGTACGACTG"
# store the match object in the variable m
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
print("entire match: " + m.group())
print("first bit: " + m.group(1))
print("second bit: " + m.group(2))

# Getting a position that match
dna = "ATGACGTACGTACGACTG"
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
print("start: " + str(m.start()))
print("end: " + str(m.end()))

dna = "ATGACGTACGTACGACTG"
m = re.search(r"GA([ATGC]{3})AC([ATGC]{2})AC", dna)
print("start: " + str(m.start()))
print("end: " + str(m.end()))
print("group one start: " + str(m.start(1)))
print("group one end: " + str(m.end(1)))
print("group two start: " + str(m.start(2)))
print("group two end: " + str(m.end(2)))

# Spliting a string using a regular expression
dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
runs = re.split(r"[^ATGC]", dna)
print(runs)

# FInding multiple matches
dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.findall(r"[AT]{4,100}", dna)
print(runs)

dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.finditer(r"[AT]{3,100}", dna)
for match in runs:
    run_start = match.start()
    run_end = match.end()
    print("AT rich region from " + str(run_start) + " to " + str(run_end))
