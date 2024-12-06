import sys

N = int(input())

array = [int(sys.stdin.readline().strip()) for _ in range(N)]
array.sort()

for i in array:
    print(i)