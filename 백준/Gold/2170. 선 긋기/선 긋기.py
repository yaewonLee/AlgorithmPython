import sys

input = sys.stdin.readline

N = int(input())
locations = []

for _ in range(N):
    x, y = map(int, input().split())
    locations.append((x, y))

locations.sort()
start, end = locations[0]

total_length = 0
for x, y in locations[1:]:
    if x > end:
        total_length += end - start
        start, end = x, y
    else:
        end = max(end, y)

total_length += end - start

print(total_length)