all_students = set(range(1, 31))

submitted_students = set()
for _ in range(28):
    submitted_students.add(int(input()))

result = sorted(all_students - submitted_students)

print(result[0])
print(result[1])