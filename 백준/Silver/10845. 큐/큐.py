from collections import deque
import sys

queue = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().strip()
    
    if command.startswith("push"):
        _, x = command.split()
        queue.append(int(x))
        
    elif command == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
            
    elif command == "size":
        print(len(queue))
        
    elif command == "empty":
        print(0 if queue else 1)
        
    elif command == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
            
    elif command == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
