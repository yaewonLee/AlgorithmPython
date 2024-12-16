directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(input())
maps = []
complexes = []

for _ in range(N):
    maps.append(list(map(int, input().strip())))

def dfs(x, y):
    count = 1
    maps[x][y] = 0

    for dx, dy in directions:
        nx, ny = dx + x, dy + y

        if nx >= 0 and ny >= 0 and nx < N and ny < N and maps[nx][ny] == 1:
            count += dfs(nx, ny)

    return count

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            complexes.append(dfs(i, j))

print(len(complexes))
complexes.sort()
for i in complexes:
    print(i)