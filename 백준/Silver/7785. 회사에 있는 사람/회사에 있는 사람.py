n = int(input())
list = set()

for _ in range(n):
    name, record = input().split()
    if record == "enter":
        list.add(name)
    else:
        list.remove(name)

sorted_list = sorted(list, reverse=True)

for i in sorted_list:
    print(i)