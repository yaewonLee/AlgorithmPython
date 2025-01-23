def solution(food):
    answer = ''
    
    for (index, value) in enumerate(food):
        if value % 2 == 1:            
            answer += str(index) * int((value - 1) / 2)
        else:
            answer += str(index) * int((value / 2))
            
    return answer + "0" + answer[::-1]