def solution(brown, yellow):
    i = 1
    
    while i * i <= yellow: # 약수 절반만 검사하기
        if yellow % i == 0:
            w = yellow // i # 노랑 가로 길이 후보
            h = i # 노랑 세로 길이 후보
    
        W = w + 2
        H = h + 2
        
        if (W * H) - (w * h) == brown:
            if W >= H:
                return [W, H]
            
        i += 1