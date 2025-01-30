def is_balanced(string):
    pair = {')': '(', ']': '['}
    stack = []

    for i in string:
        if i in "([":
            stack.append(i)
        elif i in ")]":
            if not stack or stack[-1] != pair[i]:
                return "no"
            stack.pop()

    return "yes" if not stack else "no"

while True:
    line = input().rstrip()
    if line == ".":
        break
    print(is_balanced(line))