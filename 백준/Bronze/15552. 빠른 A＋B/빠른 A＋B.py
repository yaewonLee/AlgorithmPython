import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)