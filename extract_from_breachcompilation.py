#!/usr/bin/python3
import os
import time

out = open("breachcomp.txt", "w", encoding="UTF-8")

for root, dirs, files in os.walk("data", topdown=False):
    for name in files:
        fpath = os.path.join(root, name)
        print(f"PARSING: {fpath}")
        
        with open(fpath, "r", encoding="UTF-8", errors="ignore") as f:
            for line in f:
                tmp = line.rstrip("\n").split(":")
                if len(tmp) > 1 and len(tmp[-1]) > 3 and not tmp[-1].startswith("$HEX"):
                    out.write(f"{tmp[-1]}\n")

out.close()

