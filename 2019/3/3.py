with open(r"2019\3\3.txt", "r") as f:
    wires = [cords for cords in f.read().split("\n")]

print(wires[0])