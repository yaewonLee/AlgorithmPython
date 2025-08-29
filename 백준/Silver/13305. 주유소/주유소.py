import sys

input = sys.stdin.readline

N = int(input().strip())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

min_price = cost[0]
total_cost = 0

for i in range(N-1):
    if cost[i + 1] < min_price:
        min_price = cost[i + 1]

    total_cost += min_price * distance[i]

print(total_cost)