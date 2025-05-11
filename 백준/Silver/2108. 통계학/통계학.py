from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
array = []

for _ in range(N):
    num = int(input())
    array.append(num)

freq = Counter(array)
max_freq = max(freq.values())

candidates = []

for key, val in freq.items():
    if val == max_freq:
        candidates.append(key)

print(round(sum(array) / N))
array.sort()
print(array[N // 2])
candidates.sort()
print(candidates[0] if len(candidates) == 1 else candidates[1])
print(max(array) - min(array))