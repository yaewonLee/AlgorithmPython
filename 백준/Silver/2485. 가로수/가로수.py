import sys
import math
from functools import reduce

N = int(sys.stdin.readline())
trees = []
arr = []

for _ in range(N):
    tree = int(sys.stdin.readline())
    trees.append(tree)

for i in range((len(trees) - 1)):
    arr.append(trees[i+1] - trees[i])

gcd = reduce(math.gcd, arr)

answer = 0
for i in arr:
    answer += ((i // gcd) -1)

print(answer)