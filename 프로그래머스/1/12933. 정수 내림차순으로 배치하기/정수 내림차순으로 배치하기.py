def solution(n):
    sorted_array = sorted(str(n), reverse=True)
    
    return int(''.join(sorted_array))