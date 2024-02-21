while(True):
    word = input()

    stack = []
    if word == '.':
        break

    for w in word:
        if w == '(':
            stack.append(w)
        if w == '[':
            stack.append(w)
        elif w == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(w)
                break
        elif w == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(w)
                break

    if not stack:
        print('yes')
    else:
        print('no')