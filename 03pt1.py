import sys

def points(path):
    x, y = (0, 0)
    for inst in path:
        direction = inst[0]
        l = int(inst[1:])
        for i in range(l):
            if direction == 'U':
                y += 1
            if direction == 'D':
                y -= 1
            if direction == 'R':
                x += 1
            if direction == 'L':
                x -= 1
            yield x, y


def closest_intersection(paths):
    p1, p2 = paths

    intersections = set(points(p1)) & set(points(p2)) - {(0,0)}
    return min(abs(x)+abs(y) for x,y in intersections)


print(closest_intersection(l.split(',') for l in sys.stdin.readlines()))
