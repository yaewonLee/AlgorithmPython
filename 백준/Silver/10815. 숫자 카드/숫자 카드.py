N = input()
cards = set(map(int, input().split()))
M = input()
numbers = list(map(int, input().split()))
answer = []

for i in numbers:
    if i in cards:
        answer.append("1")
    else:
        answer.append("0")

print(' '.join(answer))