N = int(input())
A = set(map(int, input().split()))
M = int(input())
array = list(map(int, input().split()))

result = []

for i in array:
    if i in A:
        print(1)
    else:
        print(0)