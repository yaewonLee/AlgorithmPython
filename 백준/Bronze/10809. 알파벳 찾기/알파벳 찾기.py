S = input().strip()
result = []

for char in range(ord('a'), ord('z') + 1):
    result.append(S.find(chr(char)))

print(" ".join(map(str, result)))