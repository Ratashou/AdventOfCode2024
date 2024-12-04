file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2024\Day4.txt", "r")

fullArray = []
total = 0

for line in file:
    fullArray.append(line)

i=0
while i < len(fullArray):
    fullArray[i] = fullArray[i].rstrip("\n")
    j=0
    while j < len(fullArray[i]):
        if fullArray[i][j] == "A" and i-1>=0 and i+1<len(fullArray) and j-1>=0 and j+1<len(fullArray[i]):
            if (fullArray[i+1][j+1] == "M" or fullArray[i+1][j+1] == "S") and (fullArray[i-1][j-1] == "M" or fullArray[i-1][j-1] == "S") and fullArray[i+1][j+1] != fullArray[i-1][j-1]:
                if (fullArray[i+1][j-1] == "M" or fullArray[i+1][j-1] == "S") and (fullArray[i-1][j+1] == "M" or fullArray[i-1][j+1] == "S") and fullArray[i+1][j-1] != fullArray[i-1][j+1]:
                    total+=1
            
        j+=1
    i+=1

print(total)

file.close()
