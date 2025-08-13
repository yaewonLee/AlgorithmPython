def solution(n):
    num_ones = bin(n).count('1')    
    answer = n + 1

    while True:
        num_one = bin(answer).count('1')
        
        if num_ones == num_one:
            break
        else:
            answer += 1
            continue
    
    return answer