import sys

def exec_intcode(xs):
    i = 0
    while True:
        op = xs[i]
        if op == 99:
            break
        a = xs[xs[i+1]]
        b = xs[xs[i+2]]
        result = None
        if op == 1:
            result = a + b
        if op == 2:
            result = a * b
        xs[xs[i+3]] = result
        i += 4
    return xs[0]

def part1(xs):
    xs[1] = 12
    xs[2] = 2
    return exec_intcode(xs)

def find_output(xs):
    for x in range(100):
        for y in range(100):
            ys = list(xs)
            ys[1] = x
            ys[2] = y
            res = exec_intcode(ys)
            if res == 19690720:
                return 100 * x + y

xs = [int(l.strip()) for l in sys.stdin.read().split(',')]
print(part1(list(xs)))
print(find_output(list(xs)))
