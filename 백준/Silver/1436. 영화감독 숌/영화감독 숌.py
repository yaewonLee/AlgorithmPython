import sys

input = sys.stdin.readline
N = int(input())

def nth_dooms_number(n):
    num = 666
    count = 0

    while True:
        if '666' in str(num):
            count += 1
            if count == n:
                return num
        num += 1

print(nth_dooms_number(N))