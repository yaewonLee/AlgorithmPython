import sys
import math

a1, a2 = map(int, sys.stdin.readline().split())
b1, b2 = map(int, sys.stdin.readline().split())
numerator = a1*b2 + b1*a2
denominator = a2 * b2

gcd = math.gcd(numerator, denominator)

print(numerator // gcd, denominator // gcd)