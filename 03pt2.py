import sys

def points(path):
    x, y = (0, 0)
    for inst in path:
        direction = inst[0]
        l = int(inst[1:])
        for _ in range(l):
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
    pts1 = list(points(p1))
    pts2 = list(points(p2))
    intersections = set(pts1) & set(pts2) - {(0,0)}
    return min(2 + pts1.index(p) + pts2.index(p) for p in intersections)


print(closest_intersection(l.split(',') for l in sys.stdin.readlines()))
