numbers = list(map(int, input().split()))
result = sum([x ** 2 for x in numbers])
print(result % 10)