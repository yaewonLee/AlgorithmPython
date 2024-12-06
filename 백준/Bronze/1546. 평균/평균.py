N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
result = []

for score in scores:
    result.append(score/M*100)

print(sum(result) / N)