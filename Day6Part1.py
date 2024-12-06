file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2024\Day6.txt", "r")

direction = "up"
gridList = []
for line in file:
    gridList.append(line)
    gridList[-1] = gridList[-1].rstrip("\n")
    gridList[-1] = list(gridList[-1])

i=0
j=0
foundIt = False
while i < len(gridList):
    while j < len(gridList[i]):
        if gridList[i][j] == "^":
            foundIt = True
            break
        j+=1
    if foundIt:
        break
    j=0
    i+=1

while True:
    gridList[i][j] = "X"
    if direction == "up":
        i = i - 1
        if i >= 0:
            if gridList[i][j] == "#":
                i = i + 1
                direction = "right"
        else:
            break
                
    elif direction == "right":
        j = j + 1
        if j < len(gridList[i]):
            if gridList[i][j] == "#":
                j = j - 1
                direction = "down"
        else:
            break

    elif direction == "down":
        i = i + 1
        if i < len(gridList):
            if gridList[i][j] == "#":
                i = i - 1
                direction = "left"
        else:
            break

    elif direction == "left":
        j = j - 1
        if j >= 0:
            if gridList[i][j] == "#":
                j = j + 1
                direction = "up"
        else:
            break
    
total = 0
for line in gridList:
    for character in line:
        if character == "X":
            total+=1
print(total)

file.close()
