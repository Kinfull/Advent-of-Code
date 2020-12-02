with open(r"2019\3\3.txt", "r") as f:
    wires = [cords for cords in f.read().split("\n")]

wire1_path = wires[0].split(",")
wire2_path = wires[1].split(",")

def calc_points_with_steps(path):
    curx = cury = step = 0
    directions = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}
    points = {}
    for segment in path:
        dx, dy = directions[segment[0]]
        for _ in range(int(segment[1:])):
            curx += dx
            cury += dy
            step += 1
            if (curx, cury) not in points:
                points[(curx, cury)] = step
    return points

wire1_points = calc_points_with_steps(wire1_path)
wire2_points = calc_points_with_steps(wire2_path)
intersection_points = [point for point in wire1_points if point in wire2_points]

part2 = min(wire1_points[point] + wire2_points[point] for point in intersection_points)

print(part2)