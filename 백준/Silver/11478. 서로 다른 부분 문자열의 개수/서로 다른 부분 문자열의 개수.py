import sys

# sys는 개행문자 \n이 포함되므로 제거 필요!!

S = sys.stdin.readline().strip()
n = len(S)

substrings = set()

for i in range(n):
    for j in range(i + 1, n + 1):
        substrings.add(S[i:j])

print(len(substrings))