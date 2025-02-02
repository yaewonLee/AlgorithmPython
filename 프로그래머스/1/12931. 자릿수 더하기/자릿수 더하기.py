def solution(n):
    array = list(str(n))
    answer = 0
    
    for i in array:
        answer += int(i)
    return answer