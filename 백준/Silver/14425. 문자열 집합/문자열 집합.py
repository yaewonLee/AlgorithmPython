N, M = map(int, input().split())
S = set()
words = set()
answer = 0

for _ in range(N):
    word = input().strip()
    S.add(word)

for _ in range(M):
    word = input().strip()
    if word in S:
        answer += 1

print(answer)