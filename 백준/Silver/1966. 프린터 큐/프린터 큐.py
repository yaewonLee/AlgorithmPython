from collections import deque

'''
첫 번째 줄: 문서의 개수 N, 궁금한 문서의 순서 M, 맨 왼쪽은 0번째
두 번째 줄: N개의 문서의 중요도
4 2 라면 문서의 개수는 4개, 궁금한 문서의 순서는 2번
1 2 3 4 -> 3은 두 번째로 프린트됨 = 2 출력
'''

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    priorities = list(map(int, input().split()))
    
    queue = deque((priority, idx) for idx, priority in enumerate(priorities))
    
    count = 0

    while queue:
        current = queue.popleft()
        
        if any(current[0] < doc[0] for doc in queue):  
            queue.append(current)
        else:
            count += 1
            if current[1] == M:
                print(count)
                break
