import re

file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2024\Day3.txt", "r")

total = 0
doIt = True
for line in file:
    test = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
    for muls in test:
        if "do()" in muls:
            doIt = True
        if "don't()" in muls:
            doIt = False
        if "mul" in muls and doIt:
            values = muls.split(",")
            values[0] = int(values[0].strip("mul("))
            values[1] = int(values[1].strip(")"))
            total += values[0] * values[1]

print(total)

file.close()
