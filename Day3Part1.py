import re

file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2024\Day3.txt", "r")

total = 0
for line in file:
    test = re.findall(r"mul\(\d+,\d+\)", line)
    for muls in test:
        values = muls.split(",")
        values[0] = int(values[0].strip("mul("))
        values[1] = int(values[1].strip(")"))
        total += values[0] * values[1]

print(total)

file.close()
