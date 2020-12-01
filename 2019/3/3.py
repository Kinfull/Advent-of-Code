with open(r"2019\3\3.txt", "r") as f:
    wires = [cords for cords in f.read().split("\n")]

wires1 = wires[0].split(",")
wires2 = wires[1].split(",")

wires[0] = wires1
wires[1] = wires2



y1 = 0
x1 = 0

y2 = 0
x2 = 0

firstList = wires[0]
secondList = wires[1]

x2 += int(firstList[1][1:])
print(x2)

"""
for i in range(len(wires[1])):

    if(firstList[0] == "U"):
        y1 += int(firstList[i][1:])
    elif(firstList[0] == "L"):
        x1 -= int(firstList[i][1:])
    elif(firstList[0] == "D"):
        y1 -= int(firstList[i][1:])
    elif(firstList[0] == "R"):
        x1 += int(firstList[i][1:])

    if(secondList[0] == "U"):
        y2 += int(secondList[i][1:])
    elif(secondList[0] == "L"):
        x2 -= int(secondList[i][1:])
    elif(secondList[0] == "D"):
        y2 -= int(secondList[i][1:])
    elif(secondList[0] == "R"):
        x2 += int(secondList[i][1:])
    print(x1)
"""
    #if((x1 == x2) and (y1 == y2)):
    #    print(f"firstList = {x1},{y1} secondList = {x2},{y2}")