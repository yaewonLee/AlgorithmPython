def solution(t, p):
    answer = 0
    n = len(p)
    num = int(p)
    answer = 0
    
    for i in range(0, len(t)):
        number = (t[i:i+n])
        if int(number) <= num and len(number) == n:
            answer += 1
            
    return answer