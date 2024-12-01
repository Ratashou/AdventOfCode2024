file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2024\Day1.txt", "r")

list1 = []
list2 = []
total = 0

for line in file:
    #This creates two lists, one for the left column, one for the right column
    list1.append(int(line.split()[0]))
    list2.append(int(line.split()[1]))

#Putting the lists in numerical order, lowest to highest
list1.sort()
list2.sort()

i = 0
while i < len(list1):
    #Adds the distance between the two values to the total, conveting to positive when negative
    total += abs(list1[i] - list2[i])
    i+=1

print(total)

file.close()
