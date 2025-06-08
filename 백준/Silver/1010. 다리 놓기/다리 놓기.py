import sys
import math

def combination(n, r):
    return math.comb(n, r)

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, input().split())
    print(combination(m, n))