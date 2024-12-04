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
        if fullArray[i][j] == "X":
            #Going clockwise
            #Left to right
            if j+3 < len(fullArray[i]) and fullArray[i][j+1] == "M" and fullArray[i][j+2] == "A" and fullArray[i][j+3] == "S":
                total+=1
            #Diagonal, top left to bottom right
            if j+3 < len(fullArray[i]) and i+3 < len(fullArray) and fullArray[i+1][j+1] == "M" and fullArray[i+2][j+2] == "A" and fullArray[i+3][j+3] == "S":
                total+=1
            #Top to bottom
            if i+3 < len(fullArray) and fullArray[i+1][j] == "M" and fullArray[i+2][j] == "A" and fullArray[i+3][j] == "S":
                total+=1
            #Diagonal, top right to bottom left
            if i+3 < len(fullArray) and j-3 >= 0 and fullArray[i+1][j-1] == "M" and fullArray[i+2][j-2] == "A" and fullArray[i+3][j-3] == "S":
                total+=1
            #Right to left
            if j-3 >= 0 and fullArray[i][j-1] == "M" and fullArray[i][j-2] == "A" and fullArray[i][j-3] == "S":
                total+=1
            #Diagonal, bottom right to top left
            if i-3 >= 0 and j-3 >= 0 and fullArray[i-1][j-1] == "M" and fullArray[i-2][j-2] == "A" and fullArray[i-3][j-3] == "S":
                total+=1
            #Bottom to top
            if i-3 >= 0 and fullArray[i-1][j] == "M" and fullArray[i-2][j] == "A" and fullArray[i-3][j] == "S":
                total+=1
            #Diagonal, bottom left to top right
            if i-3 >= 0 and j+3 < len(fullArray[i]) and fullArray[i-1][j+1] == "M" and fullArray[i-2][j+2] == "A" and fullArray[i-3][j+3] == "S":
                total+=1
            
        j+=1
    i+=1

print(total)

file.close()
