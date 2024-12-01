file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2024\Day1.txt", "r")

list1 = []
list2 = []
multiplier = 0
total = 0

for line in file:
    #This creates two lists, one for the left column, one for the right column
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

for line1 in list1:
    for line2 in list2:
        if line1 == line2:
            multiplier += 1
    total += line1 * multiplier
    multiplier = 0

print(total)

file.close()
