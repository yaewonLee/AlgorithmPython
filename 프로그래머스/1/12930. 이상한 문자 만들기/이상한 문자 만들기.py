def solution(s):
    result = []
    for word in s.split(" "):
        answer = ""
        for (i, value) in enumerate(word):            
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        result.append(answer)
            
    return " ".join(result)