def solution(t, p):
    answer = 0
    n = len(p)
    num = int(p)
    answer_arr = []
    
    for i in range(0, len(t)):
        number = (t[i:i+n])
        if int(number) <= num and len(number) == n:
            answer_arr.append(int(number))    
    
    return len(answer_arr)