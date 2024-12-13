import math

N = int(input())
factorial = math.factorial(N)
count = 0

for digit in reversed(str(factorial)):
    if digit == '0':
        count += 1
    else:
        break

print(count)