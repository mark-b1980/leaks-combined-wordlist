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
        if re.match(r'[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}', line):
            print(line)

            # Check format email:password
            if ":" in line:
                print(line)
                tmp = line.split(":")
                line = tmp[-1]
            else:
                line = ""

        if len(line) > 3 and len(line) < 24 and not line.startswith("$HEX"):
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

