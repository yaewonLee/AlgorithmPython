import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
MAX = 100000

def bfs(start, target):
    if start >= target:
        return start - target

    time = [-1] * (MAX + 1)
    time[start] = 0
    q = deque([start])

    while q:
        current = q.popleft()

        for next_position in (current-1, current+1, current*2):
            if 0 <= next_position <= MAX and time[next_position] == -1:
                time[next_position] = time[current] + 1
                if next_position == target:
                    return time[next_position]
                q.append(next_position)

    return time[target]

print(bfs(N, K))