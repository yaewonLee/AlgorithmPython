N = int(input())

cost = []
dp = []
R = 0
G = 1
B = 2

for i in range(N):
    r, g, b = map(int, input().split())
    cost.append([r, g, b])

for _ in range(N):
    dp.append([0, 0, 0])

# 1번집
dp[0][R] = cost[0][R]
dp[0][G] = cost[0][G]
dp[0][B] = cost[0][B]

for i in range(N):
    dp[i][R] = cost[i][R] + min(dp[i-1][G], dp[i-1][B])
    dp[i][G] = cost[i][G] + min(dp[i-1][R], dp[i-1][B])
    dp[i][B] = cost[i][B] + min(dp[i-1][R], dp[i-1][G])

print(min(dp[N-1][R], dp[N-1][G], dp[N-1][B]))