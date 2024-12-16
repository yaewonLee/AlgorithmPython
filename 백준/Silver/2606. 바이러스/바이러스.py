N = int(input())
pair = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(pair):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node] = True
    count = 0

    for current_node in graph[node]:
        if not visited[current_node]:
            count += 1
            count += dfs(current_node)

    return count

print(dfs(1))