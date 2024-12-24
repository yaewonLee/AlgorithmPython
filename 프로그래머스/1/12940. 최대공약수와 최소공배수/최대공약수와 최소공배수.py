import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def solution(n, m):
    return [math.gcd(n, m), lcm(n, m)]
