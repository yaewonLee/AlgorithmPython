import sys
sys.setrecursionlimit(10000)

T = int(input())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    maps[x][y] = 0

    for dx, dy in directions:
        nx = dx + x
        ny = dy + y

        if nx >= 0 and ny >= 0 and nx < N and ny < M and maps[nx][ny] == 1:
            dfs(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    maps = []
    count = 0

    for _ in range(N):
        maps.append([0] * M)

    for _ in range(K):
        x, y = map(int, input().split())
        maps[y][x] = 1

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)