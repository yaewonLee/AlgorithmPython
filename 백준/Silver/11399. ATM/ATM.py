N = int(input())
P = list(map(int, input().split()))

P.sort()

sum = 0
answer = 0

for i in P:
    sum += i
    answer += sum

print(answer)