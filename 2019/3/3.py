with open(r"2019\3\3.txt", "r") as f:
    wires = [cords for cords in f.read().split("\n")]

wire1 = wires[0].split(",")
wire2 = wires[1].split(",")


def Dots(input_wire):
    cordX = 0
    cordY = 0
    step = 0

    directions = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}
    points = {}

    for part in input_wire:
        dx, dy = directions[part[0]]
        for _ in range(int(part[1:])):
            cordX += dx
            cordY += dy
            step += 1
            if (cordX, cordY) not in points:
                points[(cordX, cordY)] = step
    return points

points1 = Dots(wire1)
points2 = Dots(wire2)

intersections = [dot for dot in points1 if dot in points2]
shortest = min(abs(x) + abs(y) for (x, y) in intersections)
fewest_steps = min(points1[dots] + points2[dots] for dots in intersections)

print(shortest)
print(fewest_steps)