import sys

input = sys.stdin.readline
output = sys.stdout.write

S = set()
all_set = set(range(1, 21))

M = int(input().strip())

for _ in range(M):
    command = input().strip().split()
    
    if command[0] == "add":
        S.add(int(command[1]))

    elif command[0] == "remove":
        S.discard(int(command[1]))
        
    elif command[0] == "check":
        output("1\n" if int(command[1]) in S else "0\n")

    elif command[0] == "toggle":
        num = int(command[1])
        if num in S:
            S.remove(num)
        else:
            S.add(num)

    elif command[0] == "all":
        S = all_set.copy()

    elif command[0] == "empty":
        S.clear()
