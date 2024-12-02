file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2024\Day2.txt", "r")

toTest = []
direction = ''
succeed = False
total = 0
check = 0
for line in file:
    toTest = line.split()
    i=0
    while i < len(toTest):
        toTest[i] = int(toTest[i])
        i+=1
    i=0
    while i < len(toTest):
        if i == len(toTest) - 1:
            succeed = True
            break
        if direction == 'increasing':
            if toTest[i] > toTest[i+1] or toTest[i] == toTest[i+1] or abs(toTest[i] - toTest[i+1]) > 3:
                break
        elif direction == 'decreasing' :
            if toTest[i] < toTest[i+1] or toTest[i] == toTest[i+1] or abs(toTest[i] - toTest[i+1]) > 3:
                break
        else:
            if abs(toTest[i] - toTest[i+1]) <= 3 and toTest[i] > toTest[i+1] :
                direction = 'decreasing'
            elif abs(toTest[i] - toTest[i+1]) <= 3 and toTest[i] < toTest[i+1]:
                direction = 'increasing'
            else:
                break
        i+=1
    if succeed == True:
        print(toTest)
        total += 1
    direction = ''
    succeed = False
    

print(total)

file.close()
