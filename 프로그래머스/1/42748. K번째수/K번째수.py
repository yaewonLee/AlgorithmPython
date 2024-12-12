def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = (command[0], command[1], command[2])
        
        sorted_array = array[i-1:j]
        sorted_array.sort()
        answer.append(sorted_array[k - 1])
        
    return answer