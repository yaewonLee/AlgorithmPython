N = int(input())
numberCards = list(map(int, input().split()))

M = int(input())
numbers = list(map(int, input().split()))

counts = {}

for num in numberCards:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

answer = []

for i in numbers:
    if i in counts:
        answer.append(str(counts[i]))
    else:
        answer.append('0')

print(" ".join(answer))