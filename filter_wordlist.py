#!/usr/bin/python3
import os
import re
import sys
import time

try:
    infile = sys.argv[1]
    outfile = sys.argv[2]
except:
    print("\nUSAGE:\n-------\n")
    print(f"{os.path.basename(sys.argv[0])} inputfile outputfile\n")
    exit(1)

out = open(outfile, "a", encoding="UTF-8")

with open(infile, "r", encoding="UTF-8", errors="ignore") as f:
    for line in f:
        line = line.rstrip("\n")
        # Skip emails
        if re.findall(r'[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}', line):
            #print(line)

            # Check format email:password
            if ":" in line:
                tmp = line.split(":")
                line = tmp[-1]
            
            # Check format email;password
            elif ";" in line:
                tmp = line.split(";")
                line = tmp[-1]

            # Check format email;password
            elif "||" in line:
                tmp = line.split("||")
                line = tmp[-1]

            # Set dummy value to prevent processing
            else:
                print(line)
                line = ""

        # Check for || as field delimiter in case of username||password
        if "||" in line:
            tmp = line.split("||")
            line = tmp[-1]

        # Ignore lines with $HEX[...] notation
        if line.startswith("$HEX"):
            print(line)

        # Add all 4 - 23 character lines as password
        elif len(line) > 3 and len(line) < 24:
            out.write(f"{line}\n")
        
        # Just numbers or all the same caracters
        elif line.isnumeric() or (len(line) != 0 and len(line.replace(line[0], "")) == 0):
            out.write(f"{line}\n")
        
        # Check if line is a valid hex value and exclude those
        elif len(line) > 3:
            try:
                int(f"0x{line}", 16)
                print(line)
            except:
                out.write(f"{line}\n")

out.close()

