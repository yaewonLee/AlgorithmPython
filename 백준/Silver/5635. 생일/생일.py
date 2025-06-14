n = int(input())

students = []

for _ in range(n):
    parts = input().split()
    name = parts[0]
    day = int(parts[1])
    month = int(parts[2])
    year = int(parts[3])

    students.append((year, month, day, name))

students.sort()

print(students[-1][3])

print(students[0][3])