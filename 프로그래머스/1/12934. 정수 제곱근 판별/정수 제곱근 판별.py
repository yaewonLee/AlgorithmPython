import math

def solution(n):    
    sqrt = math.isqrt(n)
    
    if sqrt * sqrt == n:
        return (sqrt + 1) * (sqrt + 1)
    else:
        return -1