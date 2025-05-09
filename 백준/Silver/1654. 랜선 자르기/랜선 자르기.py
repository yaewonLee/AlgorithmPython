K, N = list(map(int, input().split()))
lines = []

for _ in range(K):
    lines.append(int(input()))

start = 1
end = max(lines)
answer = 0

while start <= end:
    mid = (start + end) // 2
    totalLines = 0

    for line in lines:
        totalLines += line // mid

    if totalLines >= N:
        answer = mid
        # 일단 가능한 길이 저장하고 더 긴 길이 시도
        start = mid + 1
    else:
        end = mid - 1

print(answer)