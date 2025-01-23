def solution(food):
    answer = ''
    
    for (index, value) in enumerate(food):
        answer += str(index) * int((value // 2))
            
    return answer + "0" + answer[::-1]