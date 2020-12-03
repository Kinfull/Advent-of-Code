
def calc(dx, dy):
    with open(r"2020\3\3.txt", "r") as f:
        treeMap = [items for items in f.read().split("\n")[::dy]]

    treeCount = 0
    pos = 0

    for y in treeMap:
        treeCount += y[pos % len(treeMap[0])] == "#"
        pos += dx

    return treeCount

print(calc(1,1)*calc(3,1)*calc(5,1)*calc(7,1)*calc(1,2))