import sys

def fuel(m):
    return m // 3 - 2

print(sum([fuel(int(l)) for l in sys.stdin.readlines()]))