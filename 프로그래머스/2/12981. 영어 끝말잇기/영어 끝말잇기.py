def solution(n, words):
    word_set = {words[0]}
    
    for i in range(1, len(words)):
        last_letter = words[i-1][-1]
        first_letter = words[i][0]
        
        if words[i] in word_set or last_letter != first_letter:
            return [i % n + 1, i // n + 1]
        else:
            word_set.add(words[i])

    return [0,0]
    

