N = int(input())
dict = {}

for _ in range(N):
    book = input()
    if book in  dict:
        dict[book] += 1
    else:
        dict[book] = 1

max_key = max(sorted(dict), key=dict.get)
print(max_key)