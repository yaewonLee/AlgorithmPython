paper = []
for _ in range(101):
    row = []
    for _ in range(101):
        row.append(0)
    paper.append(row)

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            paper[y][x] = 1

area = 0
for row in paper:
    for value in row:
        if value == 1:
            area += 1

print(area)
