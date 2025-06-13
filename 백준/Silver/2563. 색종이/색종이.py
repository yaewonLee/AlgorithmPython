import sys

N = int(sys.stdin.readline())
grid = []

for _ in range(100):
    row = []
    for _ in range(100):
        row.append(0)
    grid.append(row)

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            grid[i][j] = 1

answer = 0

for i in grid:
    for j in i:
        if j == 1:
            answer += 1

print(answer)