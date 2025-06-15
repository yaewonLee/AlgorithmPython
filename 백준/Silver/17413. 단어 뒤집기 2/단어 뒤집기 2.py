S = list(input())
stack = []
in_tag = False
answer = []

for i in S:
    if i == '<':
        if stack:
            reversed_word = "".join(reversed(stack))
            answer.append(reversed_word)
            stack.clear()
        answer.append(i)
        in_tag = True
    elif i == '>':
        answer.append(i)
        in_tag = False
    elif in_tag:
        answer.append(i)
    elif i == ' ':
        reversed_word = "".join(reversed(stack))
        answer.append(str(reversed_word))
        answer.append(i)
        stack.clear()
    else:
        stack.append(i)
        
if stack:
    reversed_word = "".join(reversed(stack))
    answer.append(str(reversed_word))

print(''.join(answer))