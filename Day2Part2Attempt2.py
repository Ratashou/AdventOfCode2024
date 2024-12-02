file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2024\Day2.txt", "r")

template = []
toTest = []
direction = ''
succeed = False
total = 0
check = 0

for line in file:
    template = line.split()
    i=0
    while i < len(template):
        template[i] = int(template[i])
        i+=1
    toTest = template
    i=0
    j=-1
    print(template)
    while i < len(toTest):
        if i == len(toTest) - 1:
            succeed = True
            break
        if direction == 'increasing':
            if toTest[i] > toTest[i+1] or toTest[i] == toTest[i+1] or abs(toTest[i] - toTest[i+1]) > 3:
                if j < len(toTest) - 1:
                    toTest = template.copy()
                    j+=1
                    i=0
                    direction = ''
                    toTest.pop(j)
                    continue
                else:
                    break
        elif direction == 'decreasing' :
            if toTest[i] < toTest[i+1] or toTest[i] == toTest[i+1] or abs(toTest[i] - toTest[i+1]) > 3:
                if j < len(toTest) - 1:
                    toTest = template.copy()
                    j+=1
                    i=0
                    direction = ''
                    toTest.pop(j)
                    continue
                else:
                    break
        else:
            if abs(toTest[i] - toTest[i+1]) <= 3 and toTest[i] > toTest[i+1] :
                direction = 'decreasing'
            elif abs(toTest[i] - toTest[i+1]) <= 3 and toTest[i] < toTest[i+1]:
                direction = 'increasing'
            else:
                if j < len(toTest) - 1:
                    toTest = template.copy()
                    j+=1
                    i=0
                    direction = ''
                    toTest.pop(j)
                    continue
                else:
                    break
        i+=1
    if succeed == True:
        print(template)
        print(toTest)
        total += 1
    direction = ''
    succeed = False
    

print(total)

#file.close()
