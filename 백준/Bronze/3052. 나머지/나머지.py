result = set()

for _ in range(10):
    number = int(input())
    result.add(number % 42)


print(len(result))