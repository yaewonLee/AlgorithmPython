N = int(input())
info = []

for _ in range(N):
    age, name = input().split()
    info.append((int(age), name))

info.sort(key=lambda member: member[0])

for age, name in info:
    print(age, name)