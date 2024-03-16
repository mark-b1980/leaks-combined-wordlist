#!/usr/bin/python3
import os
import sys
import time

try:
    infile = sys.argv[1]
except:
    print("\nUSAGE:\n-------\n")
    print(f"{os.path.basename(sys.argv[0])} inputfile\n")
    exit(1)

#################################################################################################
# Split files for easier processing
#################################################################################################
starttime = time.time()
chars = "0123456789abcdefghijklmnopqrstuvwxyz_"
parts = {}

# Open all the output files
for c in chars:
    parts[c] = open(f"{c}.tmp", "w")

# Parse inputfile and split
byte_count = 0
last_mb = 0

with open(infile, "r", encoding="UTF-8", errors="ignore") as f:
    for line in f:
        byte_count += len(line)
        line = line.rstrip("\n")
        first_char = line[0].lower()

        # Add all symbols and other characters to _.tmp file
        if first_char not in chars:
            first_char = "_"

        # Write to the file according to first character
        parts[first_char].write(f"{line}\n")
        mb = int(byte_count / 1024 / 1024)
        if mb % 100 == 0 and last_mb != mb:
            last_mb = mb
            print(f"{mb/1024:4.1f} GB processed ...")
        
# Close all the output files
for c in chars:
    parts[c].close()


#################################################################################################
# Sorting all temp files, removing of duplicates and combining them
#################################################################################################
print()
os.system(f"rm leaks_combined.txt")

for c in chars:
    print(f"SORTING {c}.tmp")
    os.system(f"sort {c}.tmp > {c}.sorted")

    print(f"REMOVING DUPLICATES FROM {c}.tmp")
    os.system(f"uniq {c}.sorted >> leaks_combined.txt")
    #os.system(f"uniq {c}.sorted > {c}.tmp")
    os.system(f"rm {c}.sorted")
    os.system(f"rm {c}.tmp")


#################################################################################################
# Compress for upload to GitHub
#################################################################################################
print()
print(f"COMPRESSING leaks_combined.txt ...")
os.system("rm wordlist/*")
os.system("zip -s 1G wordlist/leaks_combined.zip leaks_combined.txt")
print(f"PROCESSING DONE IN: {int((time.time() - starttime) / 60)} MIN.!")
print()

