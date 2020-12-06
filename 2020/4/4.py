with open(r"2020\4\4.txt", "r") as f:
    passportList = [blocks for blocks in f.read().split("\n\n")]

for items in range(len(passportList)):
    passportList[items] = passportList[items].split(" ")
    for elements in range(len(passportList[items])):
        passportList[items] = passportList[items][elements].split("\n")

print(passportList[0][4])
