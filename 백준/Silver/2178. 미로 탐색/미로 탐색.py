from collections import deque

N, M = map(int, input().split())
graph = []
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(N):
    graph.append(list(map(int, input().strip())))

def bfs( ):
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = (dx + x), (dy + y)

            if nx >= 0 and ny >= 0 and nx < N and ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


    return graph[N - 1][M - 1]

print(bfs())