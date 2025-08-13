def solution(n):
    answer = 0
    binary_n = list(bin(n)[2:])
    num_ones = binary_n.count('1')
    answer = n + 1

    while True:
        binary = list(bin(answer)[2:])
        num_one = binary.count('1')
        
        if num_ones == num_one:
            break
        else:
            answer += 1
            continue
    
    return answer